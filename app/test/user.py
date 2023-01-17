from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()
@router.get("/user/login")
async def login():
    return HTMLResponse(content="""
    <body>
    <form action="http://localhost:8000/user/login" method="post"
    style = "width:300px; margin: 50 auto">
  
    <div class="container">
      <label for="email"><b>Username</b></label>
      <input type="text" placeholder="Enter Email" name="email" required>
        <br/>
      <label for="password"><b>Password</b></label>
      <input type="text" placeholder="Enter Password" name="psw" required>
        <br/>
      <button type="submit">Login</button>
  </form>
  </body>
  """)