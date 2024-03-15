import React from "react";
import styled from "styled-components";
import { MdHomeFilled, MdSearch } from "react-icons/md";
import { IoLibrary } from "react-icons/io5";
import  Playlists  from "./Playlists";
export default function Sidebar() {
  return (
    <Container>
      <div className="top__links">
        <div className="logo">
          <a href="https://open.spotify.com"><img src={require('./white_ni1.png')} alt="succtify"/></a>
        </div>
        <ul>
          <li>
            <MdHomeFilled />
            <span><a href="https://open.spotify.com/" style={{textDecoration: 'none', color: '#b3b3b3'}}>Home</a></span>
          </li>
          <li>
            <MdSearch />
            <span><a href="https://open.spotify.com/search" style={{textDecoration: 'none', color: '#b3b3b3'}}>Search</a></span>
          </li>
          <li>
            <IoLibrary />
            <span><a href="https://open.spotify.com/collection/playlists" style={{textDecoration: 'none', color: '#b3b3b3'}}>Your Library</a></span>
          </li>
        </ul>
      </div>
      <Playlists />
    </Container>
  );
}

const Container = styled.div`
  background-color: black;
  color: #b3b3b3;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  .top__links {
    display: flex;
    flex-direction: column;
    .logo {
      text-align: center;
      margin: 1rem 0;
      img {
        max-inline-size: 80%;
        block-size: auto;
      }
    }
    ul {
      list-style-type: none;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      padding: 1rem;
      li {
        display: flex;
        gap: 1rem;
        cursor: pointer;
        transition: 0.3s ease-in-out;
        &:hover {
          color: white;
        }
      }
    }
  }
`;
