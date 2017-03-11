/**
 * Created by baymax on 17/3/2.
 */
app.service('infoServer', infoServer);
app.service('manageServer', manageServer);

infoServer.$injector = ['$http'];
manageServer.$injector = ['$http', 'Upload'];

//
function infoServer($http) {
    var testGetAllInfo = $http.get('http://localhost:8080/getAllInfo');
    // var testGet = $http.get('http://localhost:7474/db/data/');
    // var testGet = $http.get('http://192.168.1.121:8080/getjson');
    var testPost = $http({
        method: 'POST',
        url: 'http://localhost:8080/postjson',
        // url: 'http://192.168.1.121:8080/postjson',
        data: {
            title: '123'
        }
    });
    return {
        testGetAllInfo: testGetAllInfo,
        testPost: testPost
    }
}

//管理页面服务
function manageServer($http, Upload) {
    var uploadFile = function(file){
        return(
            Upload.upload({
                url: 'http://localhost:8080/uploadFile',
                data: {file: file}
            })
        )
    };
    return{
      uploadFile: uploadFile
    }
}