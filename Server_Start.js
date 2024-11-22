const http = require('http');

const server = http.createServer((req, res) => {
    console.log(`Received a ${req.method} request for ${req.url}`);
    
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello, world!');
});

server.listen(5002, () => console.log('Server running on port 5002'));
