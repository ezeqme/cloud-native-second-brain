---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Keynote Sessions"
themes: ["Keynote Sessions"]
speakers: ["Colin Walters", "Senior Principal Software Engineer", "Red Hat", "Preethi Thomas", "Senior Manager", "Engineering", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1noNs/sponsored-keynote-application-developments-great-cloud-native-disruption-colin-walters-senior-principal-software-engineer-red-hat-preethi-thomas-senior-manager-engineering-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Application+Development%E2%80%99s+Great+Cloud+Native+Disruption+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sponsored Keynote: Application Development’s Great Cloud Native Disruption - Colin Walters, Senior Principal Software Engineer, Red Hat & Preethi Thomas, Senior Manager, Engineering, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Keynote Sessions]]
- País/cidade: United States / Salt Lake City
- Speakers: Colin Walters, Senior Principal Software Engineer, Red Hat, Preethi Thomas, Senior Manager, Engineering, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1noNs/sponsored-keynote-application-developments-great-cloud-native-disruption-colin-walters-senior-principal-software-engineer-red-hat-preethi-thomas-senior-manager-engineering-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Application+Development%E2%80%99s+Great+Cloud+Native+Disruption+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Application Development’s Great Cloud Native Disruption.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1noNs/sponsored-keynote-application-developments-great-cloud-native-disruption-colin-walters-senior-principal-software-engineer-red-hat-preethi-thomas-senior-manager-engineering-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Application+Development%E2%80%99s+Great+Cloud+Native+Disruption+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wpXl_8RckB8
- YouTube title: Sponsored Keynote: Application Development’s Great Cloud Native Di... Colin Walters & Preethi Thomas
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sponsored-keynote-application-developments-great-cloud-native-disrupti/wpXl_8RckB8.txt
- Transcript chars: 4506
- Keywords: container, podman, bootsy, operating, native, containers, security, kernel, update, development, workloads, alongside, bootsie, updates, needed, talked, together, cluster

### Resumo baseado na transcript

at Kon Chicago David E talked about how core kubernetes and kubernetes ecosystem work together to Foster the development of new workloads in Paris Fabian and Mike talked about how virtual machines can run on a cluster alongside containers and today we want to talk about extending workloads to other Cloud native environments and not only that is not only within kubernetes cluster which is why today we are announcing our intent to contribute a comprehensive set of container tools to cncf which means podman and boie are coming home

### Excerpt da transcript

at Kon Chicago David E talked about how core kubernetes and kubernetes ecosystem work together to Foster the development of new workloads in Paris Fabian and Mike talked about how virtual machines can run on a cluster alongside containers and today we want to talk about extending workloads to other Cloud native environments and not only that is not only within kubernetes cluster which is why today we are announcing our intent to contribute a comprehensive set of container tools to cncf which means podman and boie are coming home home thank you with more than 23,000 Stars thousands of users and years in production use podman is recognized for its security robustness and Innovations from its Inception pman was designed with with Keen awareness of cuberes and its leading role in the cloud palman stands for pod manager and as you know pods are the smallest Deployable unit in kuties yes podman loves kuties podman desktop is a userfriendly guey for managing pods containers and work work with kubernetes on your laptop it is simplifies the configuration of container tools providing developers simplistic onboarding for all of your container development needs with more than 1.5 million downloads used by thousands of developers like you and next I'm excited to introduce Bootsie and because I'm very creative with naming projects it stands for boot container with Bootsy you build your operating system using standard container tools and then deploy and upgrade it in place with Bootsy this lets containers go beyond applications and gives us a cloud native experience for operating systems that works across bare metal and virtualization in this demo we're building a container mge that will be bootable via Bootsie the base image already includes a kernel and with this we're able to use standard container build tools to build on top now I want to emphasize that Bootsy provides very sophisticated and Rich control over the operating system such as configuring kernel arguments and for example what we call logically Bound images to roll out agent and system workloads this uses pod man's great integration with system D and ties it to bootsy's transactional in place updates here you can see our system is booted into booty and we have that agent container running that's upgraded alongside the OS now you may be asking how did we get here how are containers bootable well come talk to us in the booth after about that in this demo we're going to dive into how day two updates work the s
