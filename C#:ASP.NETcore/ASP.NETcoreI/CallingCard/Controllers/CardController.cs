using System;
using Microsoft.AspNetCore.Mvc;
namespace CallingCard.Controllers
{
    public class CardController: Controller
    {
        // localhost:5000
        [HttpGet("")]
        public ViewResult Index()
        {
            return View();
        }
        //Get parameters 
        [HttpGet("{FirstName}/{LastName}/{Age}/{FavoriteColor}")]
        public JsonResult Json(string FirstName, string LastName, int Age, string FavoriteColor)
        {
            object userData = new
            {
                First_Name=FirstName,
                Last_Name=LastName,
                Age=Age,
                Favorite_Color=FavoriteColor
            };
            return Json(userData);
        }
    }
}