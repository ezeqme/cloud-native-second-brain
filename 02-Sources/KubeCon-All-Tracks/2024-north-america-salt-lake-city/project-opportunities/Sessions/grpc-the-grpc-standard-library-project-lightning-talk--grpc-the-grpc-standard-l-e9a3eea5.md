---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8z/grpc-the-grpc-standard-library-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=gRPC%3A+The+gRPC+%22Standard+Library%22+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# gRPC: The gRPC "Standard Library" | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8z/grpc-the-grpc-standard-library-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=gRPC%3A+The+gRPC+%22Standard+Library%22+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre gRPC: The gRPC "Standard Library" | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8z/grpc-the-grpc-standard-library-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=gRPC%3A+The+gRPC+%22Standard+Library%22+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6goN2YhSMvM
- YouTube title: gRPC: The gRPC "Standard Library" | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/grpc-the-grpc-standard-library-project-lightning-talk/6goN2YhSMvM.txt
- Transcript chars: 5291
- Keywords: server, standardized, health, channel, standard, protocol, library, functionality, checking, client, schema, clients, specific, install, servers, actually, definitions, debugging

### Resumo baseado na transcript

[Music] all right let's go ahead and get started so uh I'm Richard from the grpc project uh this talk is going to be a little bit different uh I'm going to be talking about the grpc quote unquote standard Library so for those of you who haven't used it grpc is an RPC system a specific kind of messaging system it gives you a nice way to evolve your API schemas over time and it really excels at microservice to microservice Communications so this talk is going to be

### Excerpt da transcript

[Music] all right let's go ahead and get started so uh I'm Richard from the grpc project uh this talk is going to be a little bit different uh I'm going to be talking about the grpc quote unquote standard Library so for those of you who haven't used it grpc is an RPC system a specific kind of messaging system it gives you a nice way to evolve your API schemas over time and it really excels at microservice to microservice Communications so this talk is going to be about several add-ons for grpc that help you get more out of it these add-ons are a collection of standardized RPC services with pre-built implementations that you can install on your servers to get some really nice functionality out of them collectively you can think of these as being sort of a standard library of grpc services in each programming language these are generally provided as a collection of separate packages Once you pull your desired package in as a dependency you generally just need to call a single function from it to install it on your server so the first of these Services is Health checking uh rest of does have a standardized way to say that a server is fully up and running instead people tend to Define their own ad hoc handlers for health this is why kubernetes liveness probes make you configure an HTP path and headers which are specific to the rest service your health checking but grpc Health checking is standardized and it's actually been integrated into kubernetes liveness checks uh kuet will make health check queries to your superpod using this standardized protocol another client to grpc health checking is a CLI tool called grpc debug and you can see an example usage of that there uh GC debug is going to feature pretty heavily in these slides the next standard service is pretty interesting because it's very grpc specific uh part of jpc's speed is due to its compact binary representation on The Wire protocol buffers but this means that the on the Y representation is not human readable and it's not even machine readable if you don't have access to the schema so in order to manually send rpcs with tools like grp curl or Postman you either need to have the API schema definitions on your local file system so these tools can read them and that can be a real pain or you can use our standardized reflection service the reflection Pro protocol is a way for GR a grpc server to tell clients the exact API definitions of all of the services exported by that server this allows clients to
