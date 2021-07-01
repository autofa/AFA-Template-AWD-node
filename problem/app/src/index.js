import express from "express";
import cookieSession from "cookie-session";


const app = express();
app.use(express.static("static"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cookieSession({
  name: 'session',
  keys: [Math.random().toString(16)],
}));

app.get("/restart", (req, res) => {
  if (req.socket.localAddress === req.socket.remoteAddress) {
    console.log("Restart");
    process.exit(0);
  } else {
    res.status(403);
    res.end("Only allow for localhost");
  }
});

app.use((err, req, res, next) => {
  console.log(err)
  res.redirect("index.html");
});

app.listen(process.env.PORT || 8888, () => {
  console.log("App start");
});
