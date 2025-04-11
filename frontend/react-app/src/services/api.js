import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const login = async (email, password) => {
  const response = await api.post('/api/auth/login/', { email, password });
  return response.data;
};

export const register = async (email, password) => {
  const response = await api.post('/api/auth/register/', { email, password, role: 'CLIENT' });
  return response.data;
};

export const getDevices = async () => {
  const response = await api.get('/api/devices/');
  return response.data;
};

export const registerDevice = async (name, location) => {
  const response = await api.post('/api/devices/register/', { name, location });
  return response.data;
};

export const assignUser = async (clientId, userId, role) => {
  const response = await api.post(`/api/clients/${clientId}/assign/`, { user_id: userId, role });
  return response.data;
};

export const getSensorData = async (deviceId) => {
  const response = await api.get(`/api/sensor-data/${deviceId}/`);
  return response.data;
};

export const updateSensorData = async (deviceId, data) => {
  const response = await api.patch(`/api/sensor-data/${deviceId}/update/`, data);
  return response.data;
};

export const getAlerts = async () => {
  const response = await api.get('/api/alerts/');
  return response.data;
};

export const resolveAlert = async (alertId) => {
  const response = await api.patch(`/api/alerts/${alertId}/resolve/`, { resolved: true });
  return response.data;
};

export const getDashboardData = async () => {
  const response = await api.get('/api/dashboard/data-summary/');
  return response.data;
};