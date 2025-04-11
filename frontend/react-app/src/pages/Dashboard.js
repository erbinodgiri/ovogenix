import { useEffect, useState } from 'react';
import { getDashboardData } from '../services/api';
import SensorChart from '../components/SensorChart';

function Dashboard({ user }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getDashboardData();
        setData(response);
      } catch (err) {
        console.error('Failed to fetch dashboard data');
      }
    };
    fetchData();
  }, []);

  return (
    <div className="container">
      <h2>{user.role} Dashboard</h2>
      <SensorChart data={data} />
    </div>
  );
}

export default Dashboard;