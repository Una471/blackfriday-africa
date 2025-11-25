import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getProductsByCategory } from '../services/api';
import ProductCard from '../components/ProductCard';
import SearchBar from '../components/SearchBar';

const categoryContainerStyle = {
  maxWidth: '1200px',
  margin: '0 auto',
  padding: '20px',
};

const bannerStyle = {
  backgroundColor: '#333',
  color: 'white',
  padding: '40px 20px',
  textAlign: 'center',
  marginBottom: '20px',
};

const gridContainerStyle = {
  display: 'grid',
  gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
  gap: '20px',
};

const Category = () => {
  const { categoryName } = useParams();
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!categoryName) return;

    const fetchProductsByCategory = async () => {
      try {
        setLoading(true);
        const response = await getProductsByCategory(categoryName);
        setProducts(response.data);
        setFilteredProducts(response.data);
      } catch (err)  {
        setError(`There was an error fetching products for the "${categoryName}" category.`);
        console.error("Fetch error:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchProductsByCategory();
  }, [categoryName]);

  const handleSearch = ({ searchTerm, minPrice, maxPrice, sortBy, retailer }) => {
    let filtered = products.filter((product) =>
      product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    if (minPrice) {
      filtered = filtered.filter((product) => product.price >= parseFloat(minPrice));
    }

    if (maxPrice) {
      filtered = filtered.filter((product) => product.price <= parseFloat(maxPrice));
    }

    if (retailer) {
      filtered = filtered.filter((product) => product.retailer === retailer);
    }

    if (sortBy === 'asc') {
      filtered.sort((a, b) => a.price - b.price);
    } else if (sortBy === 'desc') {
      filtered.sort((a, b) => b.price - a.price);
    }

    setFilteredProducts(filtered);
  };

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '50px' }}>Loading products...</div>;
  }

  if (error) {
    return <div style={{ textAlign: 'center', padding: '50px', color: 'red' }}>{error}</div>;
  }

  return (
    <div style={categoryContainerStyle}>
      <div style={bannerStyle}>
        <h1 style={{ textTransform: 'capitalize' }}>{categoryName}</h1>
      </div>
      <SearchBar onSearch={handleSearch} />
      {filteredProducts.length > 0 ? (
        <div style={gridContainerStyle}>
          {filteredProducts.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      ) : (
        <div style={{ textAlign: 'center', padding: '50px' }}>No products found for this category.</div>
      )}
    </div>
  );
};

export default Category;