import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10, // Number of virtual users (simulated users)
  duration: '10s', // Test duration (adjust as needed)
};

export default function () {
  let accountData = {
    account_name: 'TestAccount' + __VU,
    contact_email: 'test' + __VU + '@example.com',
  };

  let response = http.post('https://api.fluencyinc.co/account/create', JSON.stringify(accountData), {
    headers: { 'Content-Type': 'application/json' },
  });

  check(response, {
    'Account Created Successfully': (r) => r.status === 200,
  });

  sleep(1);
}
