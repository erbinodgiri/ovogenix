import { Link, useNavigate } from 'react-router-dom';

function Navbar({ user, setUser }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setUser(null);
    navigate('/login');
  };

  return (
    <nav>
      <Link to="/">Ovogenix</Link>
      {user ? (
        <>
          <Link to="/dashboard">Dashboard</Link>
          {user.role === 'CLIENT' && <Link to="/devices">Devices</Link>}
          <Link to="/alerts">Alerts</Link>
          {user.role === 'SUPER_ADMIN' && <Link to="/admin">Admin</Link>}
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <>
          <Link to="/login">Login</Link>
          <Link to="/register">Register</Link>
        </>
      )}
    </nav>
  );
}

export default Navbar;