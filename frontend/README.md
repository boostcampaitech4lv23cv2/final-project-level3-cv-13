# 🕸️Frontend
## 서버 환경 구성(Requirements)
```
# Server Environment set-ups for Streamlit at local environment

pip install pip==22.3.1
pip install -r frontend/requirements.txt
streamlit run frontend/simple_streamlit_web.py --server.fileWatcherType=none --server.port 443 --server.address 0.0.0.0 --browser.gatherUsageStats False
```
- Server 환경에서 사용할 경우 Dockerfile을 활용해서 진행
# 📋Reference
## Streamlit으로 Demo Frontend page 만들기
### Streamlit
[Streamlit GCP Setup](https://www.artefact.com/blog/how-to-deploy-and-secure-your-streamlit-app-on-gcp/)  
[Streamlit Configuration](https://docs.streamlit.io/library/advanced-features/configuration)  

## React로 Frontend page 만들기
[Create a New React App](https://reactjs.org/docs/create-a-new-react-app.html)  
[Components and props](https://ko.reactjs.org/docs/components-and-props.html)  
[Using the Public Folder](https://create-react-app.dev/docs/using-the-public-folder)  
[Conditional Rendering](https://ko.reactjs.org/docs/conditional-rendering.html)  

### React 구현
[외부 링크 삽입 방법](https://velog.io/@runprogrmm/React-%EC%99%B8%EB%B6%80-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%97%B0%EA%B2%B0%ED%95%98%EB%8A%94-%EB%B2%95)    
[SVD tag problems](https://stackoverflow.com/questions/59820954/syntaxerror-unknown-namespace-tags-are-not-supported-by-default)
### Material UI 사용
[Typography](https://react.school/material-ui/typography)  
[Typography API](https://mui.com/material-ui/api/typography/)  
[Toolbar API](https://mui.com/material-ui/api/toolbar/)  
[APP bar](https://mui.com/material-ui/react-app-bar/)      
[Card](https://mui.com/material-ui/react-card/)  
[Box](https://mui.com/material-ui/react-box/)  
[Modal](https://mui.com/material-ui/react-modal/)  
[Spacing](https://mui.com/material-ui/react-modal/)  

### npm
[Dropzone](https://react-dropzone.js.org/#section-basic-example)
[packege-lock.json?](https://pewww.tistory.com/11)

### Firebase Build
[Firebase 배포](https://blog.roto.codes/deploy-react-app-to-firebase/)

### Travis CI Build
[Firebase Travis CI](https://docs.travis-ci.com/user/deployment/firebase/#deploying-to-a-custom-project)  
[Travis CI installing dependencies](https://docs.travis-ci.com/user/deployment/firebase/#deploying-to-a-custom-project)
[Skipping deployment because this branch is not permitted](https://github.com/travis-ci/travis-ci/issues/8289)  
  
