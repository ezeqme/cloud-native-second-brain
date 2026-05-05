---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Danny Hershko Shemesh", "Alon Schindel", "Wiz"]
sched_url: https://kccncna2022.sched.com/event/182Jl/kubernetes-to-cloud-attack-vectors-demos-inside-danny-hershko-shemesh-alon-schindel-wiz
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+to+Cloud+Attack+Vectors%3A+Demos+Inside+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes to Cloud Attack Vectors: Demos Inside - Danny Hershko Shemesh & Alon Schindel, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Danny Hershko Shemesh, Alon Schindel, Wiz
- Schedule: https://kccncna2022.sched.com/event/182Jl/kubernetes-to-cloud-attack-vectors-demos-inside-danny-hershko-shemesh-alon-schindel-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+to+Cloud+Attack+Vectors%3A+Demos+Inside+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes to Cloud Attack Vectors: Demos Inside.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Jl/kubernetes-to-cloud-attack-vectors-demos-inside-danny-hershko-shemesh-alon-schindel-wiz
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+to+Cloud+Attack+Vectors%3A+Demos+Inside+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_VcmdlV6xaY
- YouTube title: Kubernetes to Cloud Attack Vectors: Demos Inside - Danny Hershko Shemesh & Alon Schindel, Wiz
- Match score: 0.781
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-to-cloud-attack-vectors-demos-inside/_VcmdlV6xaY.txt
- Transcript chars: 30281
- Keywords: cluster, security, instance, server, container, network, identity, certificate, metadata, attacker, command, default, create, resource, private, permissions, credentials, cubelet

### Resumo baseado na transcript

okay friends let's start alone please hello everyone we're really excited to be here and it's exciting to be on this stage here with me is Danny hi and this is alone and we are both from we are the fastest growing Cloud security company ever and um we realized when we started our Cloud security Journey almost three years ago that a cloud security goes and hand in hand with a kubernetes security and container security and you can't really separate both of them you can think of kubernetes Pod uh consumed resources and runtime cool our next Cloud will be Google cloud with our Google kubernetes engine now for this uh first point I would like to mention how a VM becomes a kubernetes node now a VM does a bootstrap process in so by now you're probably good now the second point is a more novel attack Vector of impersonating two kubernetes system components Cube proxy and node problem detector now if you recall I mentioned the Cuban's metadata property and it turns out it contains a few more surprises now I'll use gcloud CLI again to list instance templates and down below let us Zone in on these two tokens the node proxy code the Q proxy token and the problem detector token these are static tokens that can be used read services and endpoints and the nodes create patch or update kubernetes events and read endpoint slices great the node problem detector role is the second one it gives...

### Excerpt da transcript

okay friends let's start alone please hello everyone we're really excited to be here and it's exciting to be on this stage here with me is Danny hi and this is alone and we are both from we are the fastest growing Cloud security company ever and um we realized when we started our Cloud security Journey almost three years ago that a cloud security goes and hand in hand with a kubernetes security and container security and you can't really separate both of them you can think of kubernetes as a cloud within the cloud because you have for both of them you have identity model you have networking model you have storage model for each one of them and you have I mean they are different and you have to control each one of them in order to secure them properly and you also have the interfaces between both of them and you also have to know these interface as well a misconfigured container can lead to a lateral movement to your Cloud environment and a network exposure issue in your Cloud environment can put your container at risk now today when when organizations build most of their modern organization build their um their applications on top of kubernetes you have to really understand well both of them and how to uh both of these domains and they can't be separated you need to address both of them so today what what uh Danny is is going to to show he's going to demonstrate few examples of these this interface between cloud and kubernetes and will also help you understand how to to secure both of them properly but we really want you to take away from this to this talk that it's these two domains the cloud security and kubernetes security cannot be separated and on a personal note it's really dummy is really amazing and is an amazing expert to this the to this topic so I know we work in the same company but it's really a privilege to be here and hear all these examples today and we're now no pressure Danny let's go okay um cool so uh hello everyone uh so this is the kubernetes to Cloud attack vectors presentation now I do want to note that this is a lighter much lighter version of this presentation uh and we got the full version in the kubecon's website and I invite you all to download the full uh presentation there so friends we flew 16 hours over here from Tel Aviv to warn you about that that there are many kubernetes to Cloud integration points in these seals that there are many attack vectors on both sides of the equation and when you use a manage kubernetes soluti
