---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Operations"
themes: ["Operations"]
speakers: ["Kohei Ota", "Hewlett Packard Enterprise", "Kaslin Fields", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE2K/resource-requests-and-limits-under-the-hood-the-journey-of-a-pod-spec-kohei-ota-hewlett-packard-enterprise-kaslin-fields-google
youtube_search_url: https://www.youtube.com/results?search_query=Resource+Requests+and+Limits+Under+the+Hood%3A+The+Journey+of+a+Pod+Spec+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Resource Requests and Limits Under the Hood: The Journey of a Pod Spec - Kohei Ota, Hewlett Packard Enterprise & Kaslin Fields, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Operations]]
- Temas: [[Operations]]
- País/cidade: Virtual / Virtual
- Speakers: Kohei Ota, Hewlett Packard Enterprise, Kaslin Fields, Google
- Schedule: https://kccnceu2021.sched.com/event/iE2K/resource-requests-and-limits-under-the-hood-the-journey-of-a-pod-spec-kohei-ota-hewlett-packard-enterprise-kaslin-fields-google
- Busca YouTube: https://www.youtube.com/results?search_query=Resource+Requests+and+Limits+Under+the+Hood%3A+The+Journey+of+a+Pod+Spec+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Resource Requests and Limits Under the Hood: The Journey of a Pod Spec.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2K/resource-requests-and-limits-under-the-hood-the-journey-of-a-pod-spec-kohei-ota-hewlett-packard-enterprise-kaslin-fields-google
- YouTube search: https://www.youtube.com/results?search_query=Resource+Requests+and+Limits+Under+the+Hood%3A+The+Journey+of+a+Pod+Spec+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WB3_sV_EQrQ
- YouTube title: Resource Requests and Limits Under the Hood: The Journey of a Pod Spec - Kohei Ota & Kaslin Fields
- Match score: 0.932
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/resource-requests-and-limits-under-the-hood-the-journey-of-a-pod-spec/WB3_sV_EQrQ.txt
- Transcript chars: 19170
- Keywords: container, request, resource, limits, scheduler, requests, runtime, groups, vertical, resources, memory, cubelet, running, actually, containers, scaler, recommendations, assigned

### Resumo baseado na transcript

hello and welcome to kubecon cloudnativecon eu 2021 virtual this is resource requests and limits under the hood the journey of a pod spec i'm caslin fields and i'm a developer advocate at google i'm also a cloud native computing foundation ambassador and a member of the kubernetes special interest group for contributor experience i love to explain fun tech concepts with analogies and illustrations so i do that on my website at caslin.rocks and you'll see a lot of that in today's presentation you can always find me on

### Excerpt da transcript

hello and welcome to kubecon cloudnativecon eu 2021 virtual this is resource requests and limits under the hood the journey of a pod spec i'm caslin fields and i'm a developer advocate at google i'm also a cloud native computing foundation ambassador and a member of the kubernetes special interest group for contributor experience i love to explain fun tech concepts with analogies and illustrations so i do that on my website at caslin.rocks and you'll see a lot of that in today's presentation you can always find me on twitter at caslin fields and i am kohei ota i'm an architect at hewlett packard enterprise i'm also a cncf ambassador and in the communities community i'm the owner of sick doc's japanese translation so if you ever speak japanese and wants to contribute to the quran's project your per request are always welcome i go by inductor on twitter and github so that's us and let's get going today we're going to use a fun analogy to help these concepts really stick and help you remember them so to start off our analogy for our talk today i want you to think about your app being like a dog and in this case your dog is going to be going into the doggy daycare i've used this analogy before as a way to help explain container primitives that will come into play here a little bit later but the main idea i want you to get here is that your application when you put it into kubernetes for kubernetes to run is going to be running alongside lots of other applications being run in containers and our goal here is to make sure that all of our applications have everything that they need to be able to run successfully however apps don't always play nicely with each other so resource requests and limits can help us make sure that they have everything that they need without getting in each other's way and since we're talking about kubernetes kubernetes is container orchestration which means containers and applications at scale so we're going to be talking about our doggy daycare and all of the many people and pieces that make up our doggy daycare and how how kubernetes takes care of our apps essentially so let's dive into resource requests and limits first here's a look at an ordinary pod spec you may have seen one of these before here is our app our dog is going to be within the image for our container that we're actually going to be running within our pod and you can see below our container image we have defined a resource request and a resource limit so we're going to
