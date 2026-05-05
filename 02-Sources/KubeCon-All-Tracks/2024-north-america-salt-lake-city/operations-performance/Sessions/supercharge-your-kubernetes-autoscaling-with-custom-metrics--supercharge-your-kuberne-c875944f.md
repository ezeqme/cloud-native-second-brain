---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Observability", "Kubernetes Core", "SRE Reliability"]
speakers: ["Vamshi Krishna Samudrala", "Sravan Akinapally", "American Airlines"]
sched_url: https://kccncna2024.sched.com/event/1i7qe/supercharge-your-kubernetes-autoscaling-with-custom-metrics-vamshi-krishna-samudrala-sravan-akinapally-american-airlines
youtube_search_url: https://www.youtube.com/results?search_query=Supercharge+Your+Kubernetes+Autoscaling+with+Custom+Metrics+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Supercharge Your Kubernetes Autoscaling with Custom Metrics - Vamshi Krishna Samudrala & Sravan Akinapally, American Airlines

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Vamshi Krishna Samudrala, Sravan Akinapally, American Airlines
- Schedule: https://kccncna2024.sched.com/event/1i7qe/supercharge-your-kubernetes-autoscaling-with-custom-metrics-vamshi-krishna-samudrala-sravan-akinapally-american-airlines
- Busca YouTube: https://www.youtube.com/results?search_query=Supercharge+Your+Kubernetes+Autoscaling+with+Custom+Metrics+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Supercharge Your Kubernetes Autoscaling with Custom Metrics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qe/supercharge-your-kubernetes-autoscaling-with-custom-metrics-vamshi-krishna-samudrala-sravan-akinapally-american-airlines
- YouTube search: https://www.youtube.com/results?search_query=Supercharge+Your+Kubernetes+Autoscaling+with+Custom+Metrics+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LrL9tRnAH0M
- YouTube title: Supercharge Your Kubernetes Autoscaling with Custom Metrics - V. Krishna Samudrala, S. Akinapally
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/supercharge-your-kubernetes-autoscaling-with-custom-metrics/LrL9tRnAH0M.txt
- Transcript chars: 17724
- Keywords: metrics, custom, scaling, prometheus, metric, application, metrix, resource, define, adopter, server, requests, memory, external, request, customer, matrix, threshold

### Resumo baseado na transcript

let's get started yeah so a topic of supercharge your cuberes Autos Skilling with custom metrics uh myself vami samudrala Enterprise architect American Airlines for cloud engineering platforms hey I'm I'm shanali lead engineer kubernetes platform team so yeah so let's go through what we just we'll go brief across what is Autos scaling and uh there are different types of Auto scaling but we will touch BAS acoss horizontal produ to scaler and we'll just explore some custom metrics what do you mean by custom metrics and what can metrics on each node and then the cubet exposes the metrics so that it's a readable API over the API and then metric server Aggregates this data and moves it to kubernetes API under the AO right so with this the dynamic scaling happens but on the networking side so not every time you require CPU or memory to scale so there are some other requests so that's is the custom metrics custom metrics are user defined performance indicators that extend the default resources that CPU and memory uh that are supported by HPA right so beyond CPU and memory and you can see the application Level metrics such as Q length request latency or the business Rel any business data that you want to bring in uh there are some external sources also if

### Excerpt da transcript

let's get started yeah so a topic of supercharge your cuberes Autos Skilling with custom metrics uh myself vami samudrala Enterprise architect American Airlines for cloud engineering platforms hey I'm I'm shanali lead engineer kubernetes platform team so yeah so let's go through what we just we'll go brief across what is Autos scaling and uh there are different types of Auto scaling but we will touch BAS acoss horizontal produ to scaler and we'll just explore some custom metrics what do you mean by custom metrics and what can be used to scale the HPA uh and implementing that HPA with custom metrics so we'll look into two things what's promus adapter and kada and we'll have a live demos that we'll be scaling across and we will discuss about some best practices with custom metrics and if then we can go into Q&A so horizontal B is scalar with custom metrics right so it's Autos scaling is a powerful feature uh in a contain orchestration world for your applications that automatically wants to scale Up and Down based on the resource utilization right so in this we will explore HPA basically uh Autos scaling you know we have three different types of Auto scaling cluster Auto scalers uh horizontal part A scalers and vertical part Auto scalers right but how and why we use kuber Auto scaling basically for resource optimization kubernetes or any enables your applications to Scale based on your demand ensuring optimal resource utilization right and reliability improving your uh reliability and also for performance for the applications based on your traffic and resource that's why you want Auto scale and cost optimizations so most of the organizations uh will look into cost optimizations also when you don't want to run your resources we don't want to we want to shut down and just for better financial budget right and not only this but also overall user experience so there are a lot of user experience dimensions for the Autos scaling that we will look into for reducing the latency and maintaining uh consistent performance across the applications right so let's Deep dive into for the next 2 minutes into the HPA let's re about uh let's let's get some uh some things about HP right so what how does the HP work and what does it do there are three BAS basic things that it does it does monitoring and it based on the scaling policies uh it takes the scaling decisions and dynamic adjustments right so monitoring metrics HPA continuously monitors the resource utilization metrics s
