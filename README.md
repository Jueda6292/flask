# flask

* Write a Flask application that can respond to HTTP requests
* Use routes and route parameters to enable compelex requests

---

# Make an API!

Whatever concept you choose, make sure it has 3-5 **fields**. For example:

* If you are managing a music collection, you might want to keep track of the following for each album:
   * Name (e.g. "Nevermind")
   * Artist (e.g. "Nirvana")
   * Year (e.g. 1991)

* If you're herding cats, you might keep track of the following for each cat:
   * Name (e.g. "Cora")
   * Breed (e.g. "Abyssinian" or "N/A")
   * Age (e.g. 3)

Be sure to replicate all of the RESTful routes

| Action Name | Method | Path | Purpose | 
| --- | --- | --- | --- |
| **index** | **GET** | `/cats` | Shows a list of this collection |
| **show** | **GET** | `/cats/<id>` | Show details of a specific item |
| **create** | **POST** | `/cats` | Add a new item to the collection |
| **update** | **PATCH** | `/cats/<id>` | Update details of a specific item |
| **delete** | **DELETE** | `/cats/<id>` | Delete a specific item |

---

You've just created a very nice API!

![](https://media.giphy.com/media/wepUQluC5smgEd4Qz4/giphy.gif)
