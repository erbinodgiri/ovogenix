import { io } from 'socket.io-client';

const WS_URL = import.meta.env.VITE_WS_URL;

export const connectWebSocket = (onAlert) => {
  const socket = io(WS_URL, {
    path: '/ws/alerts/',
    auth: { token: localStorage.getItem('token') },
  });

  socket.on('connect', () => {
    console.log('WebSocket connected');
  });

  socket.on('alert', (data) => {
    onAlert(data);
  });

  socket.on('disconnect', () => {
    console.log('WebSocket disconnected');
  });

  return socket;
};