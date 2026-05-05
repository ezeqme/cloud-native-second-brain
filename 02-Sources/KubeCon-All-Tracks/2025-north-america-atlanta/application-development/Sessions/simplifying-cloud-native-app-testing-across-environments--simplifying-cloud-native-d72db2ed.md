---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Laurent Broudoux", "Postman", "Artur Ciocanu", "Adobe Inc"]
sched_url: https://kccncna2025.sched.com/event/27FVG/simplifying-cloud-native-app-testing-across-environments-laurent-broudoux-postman-artur-ciocanu-adobe-inc
youtube_search_url: https://www.youtube.com/results?search_query=Simplifying+Cloud+Native+App+Testing+Across+Environments+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Simplifying Cloud Native App Testing Across Environments - Laurent Broudoux, Postman & Artur Ciocanu, Adobe Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United States / Atlanta
- Speakers: Laurent Broudoux, Postman, Artur Ciocanu, Adobe Inc
- Schedule: https://kccncna2025.sched.com/event/27FVG/simplifying-cloud-native-app-testing-across-environments-laurent-broudoux-postman-artur-ciocanu-adobe-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Simplifying+Cloud+Native+App+Testing+Across+Environments+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Simplifying Cloud Native App Testing Across Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVG/simplifying-cloud-native-app-testing-across-environments-laurent-broudoux-postman-artur-ciocanu-adobe-inc
- YouTube search: https://www.youtube.com/results?search_query=Simplifying+Cloud+Native+App+Testing+Across+Environments+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RvTEYp7QyzI
- YouTube title: Simplifying Cloud Native App Testing Across Environments - Laurent Broudoux & Artur Ciocanu
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/simplifying-cloud-native-app-testing-across-environments/RvTEYp7QyzI.txt
- Transcript chars: 27643
- Keywords: dapper, application, everything, micros, probably, actually, across, provide, allows, broker, delivery, important, dependencies, portable, developer, simple, kitchen, events

### Resumo baseado na transcript

So, uh today we're going to talk about the challenges of deploying a medium to complex cloud native application across different environments from your laptop to your Kubernetes clusters or cloud service providers. And so we will introduce you to tools that provide your application superpower to transform your application to be super resilient to gain some abstraction level and those port portability. uh to be connected maybe with a cache to have much more performance and probably we also need some resiliency features. Uh in the middle layer we have the dapper runtime itself and at the lowest layer we have the compute which can be kubernetes it can be your uh on prem your own cloud provider or if you want to get uh really fancy you Dapper is kind of storage agnostic which make is a little bit different in this regard. All of that is still important with Dapper, but you can externalize them as configurations via YAML manifests which are very similar to Kubernetes manifests.

### Excerpt da transcript

Okay, thank you. Thanks for joining especially at this time. So, uh today we're going to talk about the challenges of deploying a medium to complex cloud native application across different environments from your laptop to your Kubernetes clusters or cloud service providers. And so we will introduce you to tools that provide your application superpower to transform your application to be super resilient to gain some abstraction level and those port portability. But we absolutely don't want to sacrifice the developer experience. We still want the developer being able to test with confidence and to be able to not drift across the different environments. Okay. So without further ado, let's switch to a first demonstration. Okay. So that I'll set up the scene of our demonstration. So we are we having a cloud native pizza store. Very simple application that allows you to place order for pizzas. Okay. And you can see here on the top right corner that it relies on different components. a store, a pepsa broker, a kitchen component, a delivery component.

And so here I can place an order, had a pepperoni, pizza, want a beer. I have to wait a few dozens of minutes. And you can see that the workflow is starting. So I've placed an order. The order is saved. The order is sent to the kitchen. The the pizza is prepared. Then when it is prepared, it is sent to the delivery service that is bringing the pizza um till home. Okay. So the delivery service is one mile away, one kilometer away. Okay. Now the order has been delivered and it is now complete. Very easy. Okay. And you can see this application is running on my Kubernetes cluster right here. You can see the the pods right here. Okay. So looking at an architecture diagram, logical architecture diagram. We have three microservices, three components. The store, the kitchen, the delivery. The store is calling the kitchen and delivery using a rest API. It's a synchronous blocking call. And the kitchen and delivery are sending back events once they are done with the with the preparation. And it allows the store to bring uh to send the notification back to the to the UI and the user.

And if you want to have a deep dive in this application, you can check this git repository and we also have a nice blog post on the the CNCF blog post with some uh high level details on the on the application. Okay. So this is the logical vision of the application. when I start looking what's in the box things are getting a bit more complicated
