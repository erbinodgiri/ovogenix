import { useEffect, useState } from 'react';
import { getAlerts, resolveAlert } from '../services/api';
import { connectWebSocket } from '../services/websocket';
import AlertCard from '../components/AlertCard';

function Alerts({ user }) {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const response = await getAlerts();
        setAlerts(response);
      } catch (err) {
        console.error('Failed to fetch alerts');
      }
    };
    fetchAlerts();

    const socket = connectWebSocket((alert) => {
      setAlerts((prev) => [alert, ...prev]);
    });

    return () => socket.disconnect();
  }, []);

  const handleResolve = async (alertId) => {
    try {
      await resolveAlert(alertId);
      setAlerts(alerts.map((a) => (a.id === alertId ? { ...a, resolved: true } : a)));
    } catch (err) {
      console.error('Failed to resolve alert');
    }
  };

  return (
    <div className="container">
      <h2>Alerts</h2>
      {alerts.map((alert) => (
        <AlertCard key={alert.id} alert={alert} onResolve={handleResolve} />
      ))}
    </div>
  );
}

export default Alerts;
