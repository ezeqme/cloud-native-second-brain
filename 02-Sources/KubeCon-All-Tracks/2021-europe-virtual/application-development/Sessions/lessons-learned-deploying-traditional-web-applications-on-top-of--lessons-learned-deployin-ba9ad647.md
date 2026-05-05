---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["Kubernetes Core"]
speakers: ["Marcos Bjoerkelund", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/iE4z/lessons-learned-deploying-traditional-web-applications-on-top-of-kubernetes-marcos-bjoerkelund-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+Deploying+Traditional+Web+Applications+on+Top+of+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Lessons Learned Deploying Traditional Web Applications on Top of Kubernetes - Marcos Bjoerkelund, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Marcos Bjoerkelund, VMware
- Schedule: https://kccnceu2021.sched.com/event/iE4z/lessons-learned-deploying-traditional-web-applications-on-top-of-kubernetes-marcos-bjoerkelund-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+Deploying+Traditional+Web+Applications+on+Top+of+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Lessons Learned Deploying Traditional Web Applications on Top of Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4z/lessons-learned-deploying-traditional-web-applications-on-top-of-kubernetes-marcos-bjoerkelund-vmware
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+Deploying+Traditional+Web+Applications+on+Top+of+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=plpgm12i7Hs
- YouTube title: Lessons Learned Deploying Traditional Web Applications on Top of Kubernetes - Marcos Bjoerkelund
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/lessons-learned-deploying-traditional-web-applications-on-top-of-kuber/plpgm12i7Hs.txt
- Transcript chars: 21848
- Keywords: application, container, applications, images, deploy, running, external, traditional, charts, wordpress, docker, runtime, process, inputs, instance, follow, practices, support

### Resumo baseado na transcript

hi welcome to all of you i'm marcus birklund i'm based in spain and i work at vmware which i joined via the acquisition of vietnami in 2019 today i'm going to talk about some of the lessons we have learned at binami while deploying traditional web applications on top of kubernetes this talk is structured into five parts first we will have a brief introduction next we will talk about some of the different steps you will follow if you want to deploy a traditional web application on top

### Excerpt da transcript

hi welcome to all of you i'm marcus birklund i'm based in spain and i work at vmware which i joined via the acquisition of vietnami in 2019 today i'm going to talk about some of the lessons we have learned at binami while deploying traditional web applications on top of kubernetes this talk is structured into five parts first we will have a brief introduction next we will talk about some of the different steps you will follow if you want to deploy a traditional web application on top of kubernetes afterwards we'll give some tips and good practices and discuss over some particular challenges you may find and finish the talk with an example at the end i will be here to answer any questions you may have first i wanted to talk a bit my about my company bitnami which is not part of vmware is a catalog for web applications runtimes frameworks and more that can be deployed in multiple environments platforms and formats such as container images or hand charts we have more than 10 years of experience deploying web applications on these environments in fact our catalog contains almost 100 traditional web applications and more of 20 of them can be deployed in kubernetes via hand charts let's talk a bit about traditional web applications there are so many of them incredible popular ones less popular ones etc this is just a small version of the ones that we support at minami in one of those platforms and you will easily recognize more than one logo they are not designed to work in cloud native environments the date to before that will the same thing so how can we differentiate traditional and cloud native applications i have compiled a few basic requirements that we will expect any kubernetes native apps to meet so they can be deployed without any headache traditional applications however don't usually meet one or more of these requiring work routes and hacks in some cases it might even be impossible to solve these problems let's talk about them first the applications process may be stateful share resources between them next there may be no separation between application code data and configurations not allowing to specify deployment inputs without relying on configuration files stored in the local disk the application may not be ready to be stopped at any point of time or require some time to boot up this usually happens a lot in java applications such as jenkins the application may not support horizontal scaling due to design limitations usually this happens when it
