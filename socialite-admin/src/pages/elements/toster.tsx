import { time } from 'console';
import React, { useState, useEffect } from 'react';
import { Toast } from 'react-bootstrap';

interface ToastComponentProps {
  message: string | undefined;
}

const ToastComponent: React.FC<ToastComponentProps> = ({ message }) => {
  const [showToast, setShowToast] = useState<boolean>(!!message);

  // Use useEffect to update the showToast state when a new message is received
  useEffect(() => {
    setShowToast(!!message);
  }, [message]);

  return (
    <div>
      {message && (
        <Toast
          show={showToast}
          onClose={() => setShowToast(false)}
          autohide
          delay={3000}
          className="bg-danger text-white" // Apply red background color and white text color
          style={{ position: 'fixed', top: '20px', right: '20px' }} // Position on the top-right corner
        >
          <Toast.Body>{message}</Toast.Body>
        </Toast>
      )}
    </div>
  );
};

export default ToastComponent;
