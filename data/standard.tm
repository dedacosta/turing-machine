input 10101010110100111;

status q0,q1,q2,q3;

halt q3;

(q0, 1, q1, 0, R);
(q0, 0, q1, b, L);
(q1, 1, q2, 0, R);
(q2, 1, q2, 0, H);
