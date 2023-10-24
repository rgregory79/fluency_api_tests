import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 10,
  duration: '10s',
};

export default function () {
  let response = http.get('https://api.fluencyinc.co/unauthorized_endpoint');

  check(response, {
    'Unauthorized Access Denied': (r) => r.status >= 400,
  });

  sleep(1);
}
