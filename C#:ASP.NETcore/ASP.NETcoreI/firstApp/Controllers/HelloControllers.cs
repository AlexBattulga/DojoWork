using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace firstApp.Controllers
{
    public class HelloController : Controller
    {
        [HttpGetAttribute]
        public string Index()
        {
            return "Hello World!";
        }
    }
}