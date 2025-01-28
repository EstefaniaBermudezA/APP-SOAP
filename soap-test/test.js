// test.js
const pm = require('postman-request');

function run() {
  // Ajusta la URL a la que harás la petición.
  // Si tu contenedor corre en localhost:8000, pon:
  // e.g. const CALCULADORA_URL = "http://localhost:8000";
  const CALCULADORA_URL = "http://129.159.45.150:8000";

  // Envelope SOAP de ejemplo.
  const SOAP_ENVELOPE = `<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cal="http://example.com/calculadora/">
  <soap:Body>
    <cal:multiplicacion>
      <a>10</a>
      <b>5</b>
    </cal:multiplicacion>
  </soap:Body>
</soap:Envelope>`;

  const options = {
    url: CALCULADORA_URL,
    method: 'POST',
    headers: {
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': 'http://example.com/calculadora/multiplicacion'
    },
    body: SOAP_ENVELOPE,
    timeout: 60000
  };

  pm(options, function(error, response, body) {
    if (error) {
      console.error("Error en la solicitud:", error);
      process.exit(1);
    }

    if (!response || response.statusCode !== 200) {
      console.error(`Status code esperado 200, se recibió: ${response && response.statusCode}`);
      process.exit(1);
    }

    // Validar que la respuesta contenga el resultado esperado (ej. 50)
    if (!body.includes("<resultado>50.0000000000</resultado>")) {
      console.error("La respuesta SOAP no es la esperada:\n", body);
      process.exit(1);
    }

    console.log("Monitor OK: Se recibió la respuesta SOAP esperada con resultado 50.");
    process.exit(0);
  });
}

// Ejecutar la función principal
run();
