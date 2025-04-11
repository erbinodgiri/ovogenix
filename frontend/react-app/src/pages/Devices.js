import { useEffect, useState } from 'react';
import { getDevices, registerDevice, assignUser } from '../services/api';
import DeviceCard from '../components/DeviceCard';

function Devices({ user }) {
  const [devices, setDevices] = useState([]);
  const [name, setName] = useState('');
  const [location, setLocation] = useState('');
  const [userId, setUserId] = useState('');
  const [role, setRole] = useState('CONSULTANT');

  useEffect(() => {
    const fetchDevices = async () => {
      try {
        const response = await getDevices();
        setDevices(response);
      } catch (err) {
        console.error('Failed to fetch devices');
      }
    };
    if (user.role === 'CLIENT' || user.role === 'SUPER_ADMIN') {
      fetchDevices();
    }
  }, [user]);

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const device = await registerDevice(name, location);
      setDevices([...devices, device]);
      setName('');
      setLocation('');
    } catch (err) {
      console.error('Failed to register device');
    }
  };

  const handleAssign = async (e) => {
    e.preventDefault();
    try {
      await assignUser(user.id, userId, role);
      alert('User assigned');
    } catch (err) {
      console.error('Failed to assign user');
    }
  };

  if (user.role !== 'CLIENT') return <p>Access denied</p>;

  return (
    <div className="container">
      <h2>Devices</h2>
      <form onSubmit={handleRegister}>
        <input
          type="text"
          placeholder="Device Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          required
        />
        <button type="submit">Register Device</button>
      </form>
      <form onSubmit={handleAssign}>
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="CONSULTANT">Consultant</option>
          <option value="STAFF">Staff</option>
        </select>
        <button type="submit">Assign User</button>
      </form>
      {devices.map((device) => (
        <DeviceCard key={device.device_id} device={device} />
      ))}
    </div>
  );
}

export default Devices;