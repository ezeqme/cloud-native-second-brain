---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Madhu Venugopal", "Director of Engineering", "Apple"]
sched_url: https://kccncna2025.sched.com/event/27dD5/keynote-apple-containerization-secure-private-containers-on-macos-madhu-venugopal-director-of-engineering-apple
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Apple+Containerization%3A+Secure%2C+Private+Containers+on+macOS+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Apple Containerization: Secure, Private Containers on macOS - Madhu Venugopal, Director of Engineering, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: United States / Atlanta
- Speakers: Madhu Venugopal, Director of Engineering, Apple
- Schedule: https://kccncna2025.sched.com/event/27dD5/keynote-apple-containerization-secure-private-containers-on-macos-madhu-venugopal-director-of-engineering-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Apple+Containerization%3A+Secure%2C+Private+Containers+on+macOS+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Apple Containerization: Secure, Private Containers on macOS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dD5/keynote-apple-containerization-secure-private-containers-on-macos-madhu-venugopal-director-of-engineering-apple
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Apple+Containerization%3A+Secure%2C+Private+Containers+on+macOS+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TOYlKfA5R80
- YouTube title: Keynote: Apple Containerization: Secure, Private Containers on macOS - Madhu Venugopal, Apple
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-apple-containerization-secure-private-containers-on-macos/TOYlKfA5R80.txt
- Transcript chars: 4280
- Keywords: virtual, container, machine, containers, containerization, security, resources, isolation, privacy, running, access, lightweight, kernel, please, framework, directories, minimal, libraries

### Resumo baseado na transcript

Hello everyone, my name is Madu and I'm truly excited to be here to meet you all in that conference. So in the world of container security, we had to choose between isolation through virtual machines or performance through sharing resources. For security, having the same level of virtual machine isolation should be applied to each and every container. So for security our goal has always been to provide the same isolation that large virtual machines have and apply them to each and every container that is that is started. So with a goal of security, privacy and performance with a minimal kernel, direct boot and a static purpose-built in container and running each container in its own lightweight virtual machine, we get stronger isolation, better privacy posture as well as resource efficiency.

### Excerpt da transcript

Hello everyone, my name is Madu and I'm truly excited to be here to meet you all in that conference. So in the world of container security, we had to choose between isolation through virtual machines or performance through sharing resources. We have been thinking about this problem and I'm delighted to introduce you all to the Apple containerization. This past June, our team at Apple open sourced containerization framework which enables developers to create and run Linux containers directly on their Mac with a focus on security and privacy. We introduced two key projects. One, the command line tool called container that users can install directly on their Mac to manage containers. Second, containerization framework is allows us to build solutions like the command line tool. In order to run Linux containers on Mac OS, we need to virtualize the Linux environment. The historical solution is to spawn a large virtual machine to host all the running containers and the resources are allocated to this virtual machine.

As the containers are added, the resources are divied up between these containers. And when you need to share additional directories from your files, these are files are shared with the virtual machine first before being provided to the specific container that requested the data. For security, having the same level of virtual machine isolation should be applied to each and every container. For privacy, limiting the access to the directories should be done on the per container basis. only the container requesting the access should get it and we want to hit all these goals with a highly performant experience while respecting users resources. So for security our goal has always been to provide the same isolation that large virtual machines have and apply them to each and every container that is that is started. Containerization does this by running each container in its own lightweight virtual machine and still providing subsecond startup times. When sharing directories and files, only the container requesting the access directory should have access to that.

And resources like CPU and memory, when there are no containers running, resources are not allocated at all. So I've been saying the lightweight virtual machine. So what does this mean? So this is more aligned to the microVM machine model using Apple virtualization framework. We are able to run run just the minimal devices that requires for user experience and that's it. Also we are sizing the vir
