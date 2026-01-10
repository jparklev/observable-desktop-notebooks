import "dotenv/config";

// This runs at build time - secrets stay on the server
const config = {
  message: process.env.SECRET_MESSAGE || "No secret found",
  hasApiKey: !!process.env.API_KEY,
  apiKeyPrefix: process.env.API_KEY?.slice(0, 7) + "..." || "none",
  timestamp: new Date().toISOString()
};

process.stdout.write(JSON.stringify(config, null, 2));
