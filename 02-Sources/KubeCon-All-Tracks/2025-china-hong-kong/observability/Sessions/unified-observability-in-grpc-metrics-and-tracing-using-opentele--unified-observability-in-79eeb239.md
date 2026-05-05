---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Observability"
themes: ["Observability"]
speakers: ["Purnesh Dixit", "Google"]
sched_url: https://kccncchn2025.sched.com/event/1x5jY/unified-observability-in-grpc-metrics-and-tracing-using-opentelemetry-plugin-purnesh-dixit-google
youtube_search_url: https://www.youtube.com/results?search_query=Unified+Observability+in+GRPC%3A+Metrics+and+Tracing+Using+OpenTelemetry+Plugin+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unified Observability in GRPC: Metrics and Tracing Using OpenTelemetry Plugin - Purnesh Dixit, Google

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: China / Hong Kong
- Speakers: Purnesh Dixit, Google
- Schedule: https://kccncchn2025.sched.com/event/1x5jY/unified-observability-in-grpc-metrics-and-tracing-using-opentelemetry-plugin-purnesh-dixit-google
- Busca YouTube: https://www.youtube.com/results?search_query=Unified+Observability+in+GRPC%3A+Metrics+and+Tracing+Using+OpenTelemetry+Plugin+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unified Observability in GRPC: Metrics and Tracing Using OpenTelemetry Plugin.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5jY/unified-observability-in-grpc-metrics-and-tracing-using-opentelemetry-plugin-purnesh-dixit-google
- YouTube search: https://www.youtube.com/results?search_query=Unified+Observability+in+GRPC%3A+Metrics+and+Tracing+Using+OpenTelemetry+Plugin+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_Fr10UoFI7Y
- YouTube title: Unified Observability in GRPC: Metrics and Tracing Using OpenTelemetry Plugin - Purnesh Dixit
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unified-observability-in-grpc-metrics-and-tracing-using-opentelemetry/_Fr10UoFI7Y.txt
- Transcript chars: 23262
- Keywords: metrics, attempt, observability, server, plug-in, basically, client, request, trace, traces, application, matrix, create, support, census, tracing, network, provide

### Resumo baseado na transcript

Uh today we are going to walk through uh gRPC open telemetry plug-in and how to troubleshoot gRPC services uh using it. Uh in the past uh a large monolithic app could have multiple teams working on hundreds thousands of lines of code compiled into one binary. Observability in simple words is visibility into the internal goingings uh of your microser mesh to the extent you need to you need the visibility for reliability and efficiency. For example, if something breaks in your complex mesh or is performing poorly, how do you figure out where the problem is and how you fix that problem? A critical request might be failing repeated repeatedly, but because it's just one hundreds of streams, the overall connection metrics might still look healthy and you lose that specific request level detail. So how do we uh to solve that challenge we need to have some uh sophisticated observability solutions.

### Excerpt da transcript

Uh hello everyone. Uh I am Punesh Digshit. Uh I work at Google in gRPC team and I'm the maintainer for gRPC go. Uh today we are going to walk through uh gRPC open telemetry plug-in and how to troubleshoot gRPC services uh using it. Just want a quick check. How many people use gRPC here or have heard of it or worked on it? Okay. And how many people uh use open telemetry? All right. Thank you. Uh so just a quick background on gRPC. Uh in the past uh a large monolithic app could have multiple teams working on hundreds thousands of lines of code compiled into one binary. Uh this led to long and difficult build processes, big failure domains and difficulty rolling out changes due to coordination requirement. Uh in the microservices paradigm, the same app is instead made up of many smaller binaries called microservices and each serving a much tighter role and communicating with each other over the network rather than through direct function calls. Uh but microservices introduce some complexity. uh you have to define and maintain interfaces between your client and server and you have to maintain stateful connections between them and gRPC solves both of these problems for you.

So in this picture uh the blue layer talks to the red layer which talks to the yellow layer uh and these RPCs cross network and infrastructure boundaries. uh the region shown here could be an infrastructure segment where RPCs have to cross these boundaries. But let's look at another aspect of microservices where effective use of this paradigm could be hampered by a l lack of observability. Observability in simple words is visibility into the internal goingings uh of your microser mesh to the extent you need to you need the visibility for reliability and efficiency. For example, if something breaks in your complex mesh or is performing poorly, how do you figure out where the problem is and how you fix that problem? So how do we get back what we lost using the microservices paradigm? Is there any way the infrastructure or the software components can provide that required visibility? This is where gRPC observability comes in. So people choose gRPC for its incred incredible performance. It's fast and efficient.

Uh and largely uh because of two key features. Uh first is uh binary protocol uh which is known as protocol buffers and its ability to run multiple streams of communication over a single channel which is called multiplexing. However, this very efficiency introduces a significant trade-o
