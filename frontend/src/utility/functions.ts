import axios from 'axios'

const BASE_URL = 'http://localhost:5000'

export const getMessage = (addr: string): Promise<object> => {
  const path = `${BASE_URL}/${addr}`
  return axios
    .get(path)
    .then((res) => res.data)
    .catch((error) => {
      console.error(`Error reaching ${BASE_URL}/${addr} with 'getMessage'`, error)
    })
}

export const sendMessage = (addr: string, payload: object) => {
  const path = `${BASE_URL}/${addr}`
  axios
    .post(path, payload)
    .then(() => (res) => res.data)
    .catch((error) => {
      console.error(`Error reaching ${BASE_URL}/${addr} with 'sendMessage'`, error)
      console.log(error)
    })
}
