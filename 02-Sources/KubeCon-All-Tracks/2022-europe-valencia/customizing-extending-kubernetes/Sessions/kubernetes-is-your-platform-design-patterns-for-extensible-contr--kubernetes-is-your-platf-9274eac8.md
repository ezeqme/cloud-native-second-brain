---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Rafael Fernández López", "SUSE", "Fabrizio Pandini", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/ytka/kubernetes-is-your-platform-design-patterns-for-extensible-controllers-rafael-fernandez-lopez-suse-fabrizio-pandini-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+is+Your+Platform%3A+Design+Patterns+For+Extensible+Controllers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes is Your Platform: Design Patterns For Extensible Controllers - Rafael Fernández López, SUSE & Fabrizio Pandini, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Rafael Fernández López, SUSE, Fabrizio Pandini, VMware
- Schedule: https://kccnceu2022.sched.com/event/ytka/kubernetes-is-your-platform-design-patterns-for-extensible-controllers-rafael-fernandez-lopez-suse-fabrizio-pandini-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+is+Your+Platform%3A+Design+Patterns+For+Extensible+Controllers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes is Your Platform: Design Patterns For Extensible Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytka/kubernetes-is-your-platform-design-patterns-for-extensible-controllers-rafael-fernandez-lopez-suse-fabrizio-pandini-vmware
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+is+Your+Platform%3A+Design+Patterns+For+Extensible+Controllers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I1-s7AxD1Ls
- YouTube title: Kubernetes is Your Platform: Design Patterns For Extens... Rafael Fernández López & Fabrizio Pandini
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-is-your-platform-design-patterns-for-extensible-controllers/I1-s7AxD1Ls.txt
- Transcript chars: 24926
- Keywords: controller, machine, pattern, basically, resource, plugin, binary, controllers, infrastructure, responsible, object, backup, second, contract, implementation, network, extensible, cluster

### Resumo baseado na transcript

so welcome good morning so yeah it's cool that this started so uh welcome to kubecon and today we are going to talk about when kimuras is your platform and some design patterns for extensible controllers so my name is rafael i work for suse i've been working with with kubernetes for five years and a half already and yeah i have i have contributed a little to cube admin for example and with me it's fabrizio hello everyone i'm fabrizio pandini i'm staff engineer at vmware i'm tech lead

### Excerpt da transcript

so welcome good morning so yeah it's cool that this started so uh welcome to kubecon and today we are going to talk about when kimuras is your platform and some design patterns for extensible controllers so my name is rafael i work for suse i've been working with with kubernetes for five years and a half already and yeah i have i have contributed a little to cube admin for example and with me it's fabrizio hello everyone i'm fabrizio pandini i'm staff engineer at vmware i'm tech lead in seacrest and c-class life cycle and i also work to the in the class rpi project so before starting today let's let's take a look at the problem that we are trying to solve so today more and more people are developing kubernetes extension developing a controller is becoming a mainstream practice to solve a problem in a cloud-native way you can use a tool like kuber builder operator sdk to create a kubernetes controller in few minutes and and the idea is that the controller can watch a customer resource and basically reconcile the state of your system to the to the to the desired state that you define in the spec this is great we we all know this uh this pattern but what happened when your business problems became complex basically you get to align that every developer must cross where your controller alone is not enough to solve the problem so today presentation is about sharing some pattern some lesson learned about how to cross this line and i before starting i i will just to point out that what we are showing today is based on experience the business periods of rafael working on projects like cuba warden is basing on experience that we learned in cluster api and there are also some idea on how we can improve this in the future yeah so now that the premium statement is clear um it's fine to start introducing the prior the the answer to the to the question or to the problem and so when we are designing extensible controllers there are mainly two ways to do that and one way is to extend the capabilities of a single controller but that quickly gets out of hand because it's hard to maintain it's it's hard to keep track of everything and the other uh it's in case you need more than you can have more than one controller in order to reconcile all these resources but then you need to you need to keep track of of everything and they need you need to orchestrate them somehow so in the next slides uh what we are going to do is to check this last part for now so before starting let's
