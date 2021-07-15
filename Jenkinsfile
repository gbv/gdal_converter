node {
    def app

    stage('Pull!') {
        checkout scm
    }

    stage('Build It Up!'){
        app = docker.build("trappgbv/gdal_converter")
    }

    stage('Push It! (really hard)'){
        docker.withRegistry('https://registry.hub.docker.com', 'b1c76749-33e4-4496-9bf3-cd1c515ac89c') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}