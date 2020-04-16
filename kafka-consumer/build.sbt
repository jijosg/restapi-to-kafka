ThisBuild / scalaVersion     := "2.12.10"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.jijo"

lazy val root = (project in file("."))
  .settings(
    name := "kafka-consumer",
    libraryDependencies += "org.apache.kafka" %% "kafka" % "2.4.1",
    libraryDependencies += "org.apache.kafka" % "kafka-clients" % "2.4.1"
  )
