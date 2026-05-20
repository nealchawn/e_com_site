const BASE_URL = import.meta.env.VITE_BASE_URL

function ProductCard({product}) {
  return (
    <div className="bg-white rounded-xl shadow-md hover:shadow-lg">
      <img
      src = {`${BASE_URL}${product.image}`}
      alt = {product.name}
      className="w-full h-56 object-cover rounded-lg mb-4"
      />
      <h2 className="text-lg font-semibold text-grey-800 truncate">{product.name}</h2>
      <p className="text-grey-600 font-medium">${product.price}</p>
    </div>
  )
}

export default ProductCard;