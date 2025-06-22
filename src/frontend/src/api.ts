import axios from 'axios';

const API_BASE = "/api"

export const fetchRandomImage = async () => {
    const res = await axios.get(`${API_BASE}/image/random`)
    return res.data
}
