import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './chorus-lapilli.jsx'

const root = createRoot(document.getElementById("root"));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);