import { useEffect, useState } from 'react';
import { getDevices, getAlerts } from '../services/api';

function AdminPanel({ user }) {
  const [devices, setDevices] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const devResponse = await getDevices();
        const alertResponse = await getAlerts();
        setDevices(devResponse);
        setAlerts(alertResponse);
      } catch (err) {
        console.error('Failed to fetch admin data');
      }
    };
    if (user.role === 'SUPER_ADMIN') {
      fetchData();
    }
  }, [user]);

  if (user.role !== 'SUPER_ADMIN') return <p>Access denied</p>;

  return (
    <div className="container">
      <h2>Admin Panel</h2>
      <h3>Devices</h3>
      {devices.map((device) => (
        <div key={device.device_id} className="card">
          <p>{device.name} - {device.location}</p>
        </div>
      ))}
      <h3>Alerts</h3>
      {alerts.map((alert) => (
        <div key={alert.id} className="card">
          <p>{alert.message} - {alert.device_id}</p>
        </div>
      ))}
    </div>
  );
}

export default AdminPanel;