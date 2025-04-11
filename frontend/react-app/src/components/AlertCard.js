function AlertCard({ alert, onResolve }) {
    return (
      <div className="card">
        <h3>{alert.message}</h3>
        <p>Device: {alert.device_id}</p>
        <p>Type: {alert.type}</p>
        <p>Created: {new Date(alert.created_at).toLocaleString()}</p>
        {!alert.resolved && <button onClick={() => onResolve(alert.id)}>Resolve</button>}
      </div>
    );
  }
  
  export default AlertCard;
  