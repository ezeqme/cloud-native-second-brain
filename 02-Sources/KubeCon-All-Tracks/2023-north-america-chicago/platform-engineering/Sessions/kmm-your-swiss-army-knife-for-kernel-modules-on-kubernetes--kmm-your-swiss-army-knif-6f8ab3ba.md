---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Quentin Barrand", "Red Hat", "Hersh Pathak", "Intel"]
sched_url: https://kccncna2023.sched.com/event/1R2v3/kmm-your-swiss-army-knife-for-kernel-modules-on-kubernetes-quentin-barrand-red-hat-hersh-pathak-intel
youtube_search_url: https://www.youtube.com/results?search_query=KMM%3A+Your+Swiss+Army+Knife+for+Kernel+Modules+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# KMM: Your Swiss Army Knife for Kernel Modules on Kubernetes - Quentin Barrand, Red Hat & Hersh Pathak, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Quentin Barrand, Red Hat, Hersh Pathak, Intel
- Schedule: https://kccncna2023.sched.com/event/1R2v3/kmm-your-swiss-army-knife-for-kernel-modules-on-kubernetes-quentin-barrand-red-hat-hersh-pathak-intel
- Busca YouTube: https://www.youtube.com/results?search_query=KMM%3A+Your+Swiss+Army+Knife+for+Kernel+Modules+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre KMM: Your Swiss Army Knife for Kernel Modules on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2v3/kmm-your-swiss-army-knife-for-kernel-modules-on-kubernetes-quentin-barrand-red-hat-hersh-pathak-intel
- YouTube search: https://www.youtube.com/results?search_query=KMM%3A+Your+Swiss+Army+Knife+for+Kernel+Modules+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5-JQNRdX-YY
- YouTube title: KMM: Your Swiss Army Knife for Kernel Modules on Kubernetes - Quentin Barrand, Hersh Pathak
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kmm-your-swiss-army-knife-for-kernel-modules-on-kubernetes/5-JQNRdX-YY.txt
- Transcript chars: 29895
- Keywords: actually, gpu, modules, module, kernel, available, driver, hardware, version, running, loaded, enabling, create, essentially, seconds, everything, deploy, device

### Resumo baseado na transcript

um you so ready to go yeah ready to go all right hi everyone my name is H I'm from Intel excited to be here and my name is Quenton I'm from Red Hut and today we're going to talk about kmm which is indeed your Swiss Army knif for Kel modules on on kubernetes um this is what we're going to cover today um we'll start with an introduction about Kel modules what they are what purpose do they serve um and also the pain points in using them the logs Sor build logs yeah yes we want the build logs so they on the right uh let's see what's going on there okay yeah so we are I think yeah we're done loading all the packages now now we did download all the

### Excerpt da transcript

um you so ready to go yeah ready to go all right hi everyone my name is H I'm from Intel excited to be here and my name is Quenton I'm from Red Hut and today we're going to talk about kmm which is indeed your Swiss Army knif for Kel modules on on kubernetes um this is what we're going to cover today um we'll start with an introduction about Kel modules what they are what purpose do they serve um and also the pain points in using them in kubernetes environments then we'll talk about the km operator what it is and how it solves those problems um then up to you AR yeah so then we'll talk about a real world use case right enabling Intel gpus within kubernetes and we'll follow that up by taking kmm on a test drive and we're going to run a stable diffusion G de stable diffusion demo text to image with an k m m enabled Intel GPU back to you um yeah so stay tuned for more explanations about that that image here um then a few words about kmm 2.0 which will be uh uh coming later this month uh and then finally uh some qna if we if we still have time um all right so let's start with an introduction about Kel modules what they are and and why you you potentially need them um a kernel module is C code really that extends the functionality of the of the Linux kernel um so you you're likely to you're going to need those functionalities for um anything that's a driver um so for example Hardware drivers uh you know virtual file systems uh canel modules can also add cises uh to your canel so so this is where you're going to encounter those modules uh the thing is the the canal modules are um built for a specific Canal version the technically an Abi but um yeah you you need to build them really against a specific set of headers for for one Canal version um in most distributions today the can modules can be unloaded uh from the system so you will you will be able to load them and unload them that's not always the case um and finally something important is that the um the Canon modules need to be signed on secure boot enabled systems so in short if you've been using any of these things uh so we have a we have a GPU here uh we have a ni we have an accelerator uh we have five systems so if you've been using any of that then you're likely to need uh Kel modules in your setup and so the problem is that using kernel modules on on kubernetes setups has proven quite difficult over the years um you know all Canon modules ideally should be contributed Upstream um but that that's very ve
