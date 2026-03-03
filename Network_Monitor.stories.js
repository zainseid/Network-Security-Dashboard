export default {
  title: 'FAIRDEAL/Network-Automation',
};

export const PortMonitor = () => {
  const rootId = 'port-monitor-root';

  const updateUI = async () => {
    try {
      const response = await fetch('http://192.168.47.70:5001/network-ports');
      const ports = await response.json();

      const rows = ports.map(p => {
        const isCritical = p.usage > 85 || p.status === 'DOWN';
        const barColor = p.intf.includes("AD") ? '#8b5cf6' : (p.usage > 85 ? '#ef4444' : '#3b82f6');

        return `
          <tr style="border-bottom: 1px solid #edf2f7;">
            <td style="padding: 15px;">
              <div style="font-weight: bold; color: #2d3748;">${p.intf}</div>
              <div style="font-size: 11px; color: #a0aec0;">${p.ip}</div>
            </td>
            <td style="padding: 15px; width: 220px;">
              <div style="background: #edf2f7; height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="width: ${p.usage}%; background: ${barColor}; height: 100%; transition: width 0.6s ease;"></div>
              </div>
              <div style="font-size: 10px; margin-top: 4px; text-align: right;">${p.usage}% Load</div>
            </td>
            <td style="padding: 15px;">
              <span style="padding: 4px 8px; border-radius: 12px; font-size: 11px; font-weight: bold; 
                background: ${p.status === 'UP' ? '#f0fff4' : '#fff5f5'}; 
                color: ${p.status === 'UP' ? '#38a169' : '#e53e3e'};">
                ${p.status} ${isCritical ? '⚠️' : ''}
              </span>
            </td>
          </tr>
        `;
      }).join('');

      document.getElementById(rootId).innerHTML = `
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); font-family: sans-serif;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h2 style="margin: 0; color: #1a365d; font-size: 1.25rem;">Infrastructure Health Monitor</h2>
            <span style="font-size: 12px; color: #718096;">Live Updates Active</span>
          </div>
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="text-align: left; color: #4a5568; font-size: 13px; border-bottom: 2px solid #edf2f7;">
                <th style="padding: 10px;">Resource</th>
                <th style="padding: 10px;">Traffic Usage</th>
                <th style="padding: 10px;">Status</th>
              </tr>
            </thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      `;
    } catch (err) {
      document.getElementById(rootId).innerHTML = `<div style="color:red">Connecting to API at 192.168.47.70:5001...</div>`;
    }
  };

  setInterval(updateUI, 3000);
  return `<div id="${rootId}">Initializing Integrated Dashboard...</div>`;
};
