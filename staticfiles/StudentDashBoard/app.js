// Minimal JS to exercise the API endpoints
(() => {
  const tokensEl = document.getElementById('tokens');
  const rawEl = document.getElementById('raw');
  const studentsOut = document.getElementById('students-output');
  const teachersOut = document.getElementById('teachers-output');

  let access = null;
  let refresh = null;

  function log(msg) {
    const time = new Date().toLocaleTimeString();
    rawEl.textContent = `[${time}] ${msg}\n` + rawEl.textContent;
  }

  function updateTokenView() {
    tokensEl.textContent = JSON.stringify({ access, refresh }, null, 2);
  }

  async function obtainToken() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    log('POST /api/token/');
    const res = await fetch('/api/token/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const json = await res.json();
    log(`status ${res.status}`);
    if (res.ok) {
      access = json.access;
      refresh = json.refresh;
      updateTokenView();
    } else {
      log(JSON.stringify(json));
    }
  }

  async function refreshAccess() {
    if (!refresh) {
      alert('No refresh token. Obtain a token first.');
      return;
    }
    log('POST /api/token/refresh/');
    const res = await fetch('/api/token/refresh/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh })
    });
    const json = await res.json();
    log(`status ${res.status}`);
    if (res.ok) {
      access = json.access;
      updateTokenView();
    } else {
      log(JSON.stringify(json));
    }
  }

  function authHeaders() {
    const h = { 'Content-Type': 'application/json' };
    if (access) h['Authorization'] = `Bearer ${access}`;
    return h;
  }

  async function listStudents() {
    log('GET /students/');
    const res = await fetch('/students/', { headers: authHeaders() });
    const json = await res.json();
    studentsOut.textContent = JSON.stringify(json, null, 2);
    log(`status ${res.status}`);
  }

  async function createStudent() {
    const name = document.getElementById('student-name').value;
    const email = document.getElementById('student-email').value;
    const payload = { name, email };
    log('POST /students/ ' + JSON.stringify(payload));
    const res = await fetch('/students/', {
      method: 'POST',
      headers: authHeaders(),
      body: JSON.stringify(payload)
    });
    const json = await res.json();
    studentsOut.textContent = JSON.stringify(json, null, 2);
    log(`status ${res.status}`);
  }

  async function listTeachers() {
    log('GET /teachers/');
    const res = await fetch('/teachers/', { headers: authHeaders() });
    const json = await res.json();
    teachersOut.textContent = JSON.stringify(json, null, 2);
    log(`status ${res.status}`);
  }

  async function createTeacher() {
    const name = document.getElementById('teacher-name').value;
    const email = document.getElementById('teacher-email').value;
    const payload = { name, email };
    log('POST /teachers/ ' + JSON.stringify(payload));
    const res = await fetch('/teachers/', {
      method: 'POST',
      headers: authHeaders(),
      body: JSON.stringify(payload)
    });
    const json = await res.json();
    teachersOut.textContent = JSON.stringify(json, null, 2);
    log(`status ${res.status}`);
  }

  document.getElementById('btn-obtain').addEventListener('click', obtainToken);
  document.getElementById('btn-refresh').addEventListener('click', refreshAccess);
  document.getElementById('btn-list-students').addEventListener('click', listStudents);
  document.getElementById('btn-create-student').addEventListener('click', createStudent);
  document.getElementById('btn-list-teachers').addEventListener('click', listTeachers);
  document.getElementById('btn-create-teacher').addEventListener('click', createTeacher);

  updateTokenView();
})();
