---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Kubernetes Core"]
speakers: ["Helen George", "João Pereira", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/ieTQ/sponsored-session-kubernetes-package-management-using-unix-philosophy-with-carvel-helen-george-joao-pereira-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Kubernetes+Package+Management+Using+Unix+Philosophy+with+Carvel+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Session: Kubernetes Package Management Using Unix Philosophy with Carvel - Helen George & João Pereira, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Helen George, João Pereira, VMware
- Schedule: https://kccnceu2021.sched.com/event/ieTQ/sponsored-session-kubernetes-package-management-using-unix-philosophy-with-carvel-helen-george-joao-pereira-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Kubernetes+Package+Management+Using+Unix+Philosophy+with+Carvel+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Session: Kubernetes Package Management Using Unix Philosophy with Carvel.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/ieTQ/sponsored-session-kubernetes-package-management-using-unix-philosophy-with-carvel-helen-george-joao-pereira-vmware
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Kubernetes+Package+Management+Using+Unix+Philosophy+with+Carvel+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yjr9s-aLHjU
- YouTube title: Sponsored Session: Kubernetes Package Management Using Unix with Carvel, Helen George & João Pereira
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-session-kubernetes-package-management-using-unix-philosophy/Yjr9s-aLHjU.txt
- Transcript chars: 21043
- Keywords: package, software, repository, bundle, carvel, consumer, custom, installed, application, cluster, capcontroller, install, producer, resource, deploy, version, resources, packages

### Resumo baseado na transcript

Hello KubeCon, we are super excited to be here today and today we'll be talking about Kubernetes package management using Unix philosophy with Carvel. Before that worked at Pivotal Labs which was acquired by VMware and worked at ThoughtWorks which is a software consultancy. So Kubernetes ecosystem has a lot of tools that help people do all the tasks needed and a lot of these tools do more or less the same things. So this can be like a very cumbersome task and also another problem that we saw that is very cumbersome is that the person that is consuming software will have to know somehow and have to download newer versions of the software and we're trying to address this with Carvel. And as the diagram suggests, CapController allows the software producers to choose variety of underlying tools whether that may be Carvel or any other Kubernetes tools for managing the life cycle of the clusters. But for the consumer, software consumer, it only exposes CapController which simplifies the cumbersome task of using multiple tools for life cycle management as we stated in the problem statement.

### Excerpt da transcript

Hello KubeCon, we are super excited to be here today and today we'll be talking about Kubernetes package management using Unix philosophy with Carvel. A quick introduction of ourselves. My name is Helen George. I'm a product manager at VMware. I've been with VMware for a little over a year now. Before that worked at Pivotal Labs which was acquired by VMware and worked at ThoughtWorks which is a software consultancy. I've built products for a variety of customers from health care, travel, finance and retail. I'm Joel, I'm an engineer on the Carvel team. I'm also in VMware for roughly a year. I came from Pivotal software where I worked with cloud native build packs and I helped build products like Kbuild and pack. Okay, so let's see our agenda for today. We will start with talking about the the problem statement that brings us here today and afterwards we'll introduce Carvel our tool suite. Afterwards we'll see a little bit we'll see a demo of how my Carvel help with the problem that we are that we see today and then we'll be opening for some questions.

Do you want to take it away? Yeah, so today's problem statement is as follow. Getting software installed and keeping it updated on a Kubernetes cluster in a secure, scalable and automated way is cumbersome. Before we dive into solving this problem, Joel, could you tell us why this is a cumbersome task? Yes, definitely. So Kubernetes ecosystem has a lot of tools that help people do all the tasks needed and a lot of these tools do more or less the same things. So you have multiple tools for templating, multiple tools for installing software and so on and if you are a person that is producing your software, you want to have access to all the tools that all these tools and use the ones that make more sense for you. But if you're someone that is consuming software and if you have let's imagine 100 applications, you'd have to know all the tools from the ecosystem in order to manage the the your clusters. So this can be like a very cumbersome task and also another problem that we saw that is very cumbersome is that the person that is consuming software will have to know somehow and have to download newer versions of the software and we're trying to address this with Carvel.

So what is Carvel? Let's talk a little bit about Carvel. Carvel is a set of tools, suite of tools that do very targeted operations and so they are very small but they do one thing and they do it in a good way. What we're trying to do with Carve
