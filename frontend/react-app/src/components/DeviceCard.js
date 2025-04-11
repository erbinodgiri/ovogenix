function DeviceCard({ device }) {
    return (
      <div className="card">
        <h3>{device.name}</h3>
        <p>ID: {device.device_id}</p>
        <p>Location: {device.location}</p>
        <p>Registered: {new Date(device.registered_at).toLocaleString()}</p>
      </div>
    );
  }
  
  export default DeviceCard;