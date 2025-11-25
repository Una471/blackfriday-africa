import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'; // Use environment variable

const apiClient = axios.create({
  baseURL: API_URL,
});

export const getProducts = () => {
  return apiClient.get('/products');
};

export const getProductsByCategory = (category) => {
  return apiClient.get(`/products?category=${category}`);
};

export const getRetailers = () => {
  return apiClient.get('/retailers');
};

export const getCategories = () => {
  return apiClient.get('/categories');
};
