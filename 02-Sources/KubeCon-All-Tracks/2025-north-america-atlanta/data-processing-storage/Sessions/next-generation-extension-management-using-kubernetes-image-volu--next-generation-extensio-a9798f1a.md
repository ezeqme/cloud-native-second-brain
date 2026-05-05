---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Andrew L'Ecuyer", "Snowflake"]
sched_url: https://kccncna2025.sched.com/event/27Fdp/next-generation-extension-management-using-kubernetes-image-volumes-andrew-lecuyer-snowflake
youtube_search_url: https://www.youtube.com/results?search_query=Next+Generation+Extension+Management+Using+Kubernetes+Image+Volumes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Next Generation Extension Management Using Kubernetes Image Volumes - Andrew L'Ecuyer, Snowflake

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Andrew L'Ecuyer, Snowflake
- Schedule: https://kccncna2025.sched.com/event/27Fdp/next-generation-extension-management-using-kubernetes-image-volumes-andrew-lecuyer-snowflake
- Busca YouTube: https://www.youtube.com/results?search_query=Next+Generation+Extension+Management+Using+Kubernetes+Image+Volumes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Next Generation Extension Management Using Kubernetes Image Volumes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fdp/next-generation-extension-management-using-kubernetes-image-volumes-andrew-lecuyer-snowflake
- YouTube search: https://www.youtube.com/results?search_query=Next+Generation+Extension+Management+Using+Kubernetes+Image+Volumes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dGGWoFBBkgk
- YouTube title: Next Generation Extension Management Using Kubernetes Image Volumes - Andrew L'Ecuyer, Snowflake
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/next-generation-extension-management-using-kubernetes-image-volumes/dGGWoFBBkgk.txt
- Transcript chars: 32325
- Keywords: postgres, extensions, extension, volumes, postgrez, screen, server, simply, volume, specific, development, exactly, additional, setting, images, running, benefits, powerful

### Resumo baseado na transcript

And as I get underway today, I just want to quickly note how great it is to be here in Atlanta for another CubeCon surrounded by so much continued excitement and innovation around Kubernetes. And that's also why I'm so excited to be giving this specific talk today because it highlights exactly how innovation in Kubernetes continues to influence some of the most mature and widely used software in some incredibly powerful ways. By the end of this talk, my goal is that you will not only walk away with a streamlined and effective approach for getting your users the Postgres extensions they want and need, but I also want to end with a note about what this means for the Kubernetes platform and ecosystem as a whole. More specifically, I want to highlight how Kubernetes continues to influence the software we build in incredible new ways, sometimes 10 or even 20 plus years after its creation, as is the case for Postgres, as you will see today. So with that, let's now dig into exactly how Kubernetes image volumes enable a powerful new strategy for building, managing, and consuming Postgres extensions in your Kubernetes-based Postgres deployments. For instance, extensions can enable specialized data types and functions, additional security and logging, um integrations with external systems, improved administration and management capabilities, support for additional languages within...

### Excerpt da transcript

Okay, good morning and thank you for joining me today. And as I get underway today, I just want to quickly note how great it is to be here in Atlanta for another CubeCon surrounded by so much continued excitement and innovation around Kubernetes. And that's also why I'm so excited to be giving this specific talk today because it highlights exactly how innovation in Kubernetes continues to influence some of the most mature and widely used software in some incredibly powerful ways. So with that quick intro out of the way, welcome to my talk on next generation extension management using Kubernetes image volumes. And I'll start with a quick note about myself. My name is Andrew Lure and I manage the team behind PGO the Postgres operator for Kubernetes. I've been involved in the PGO project for over seven years now. And during this time I've been fortunate to experience just how far Kubernetes has come from its humble beginnings managing stateful applications. And as Kubernetes only continues to mature and grow, it feels like we're at a real inflection point where Kubernetes not only supports the deployment of our favorite and most needed applications, but it's now directly enhancing the capabilities of those applications as well as you will see today.

And I'll start out by noting that when I mention next generation extension management in the title of this talk, I'm specifically referring to the management of Postgres extensions. And for this talk today, I'm excited to highlight how two powerful new features, one in Kubernetes and one in the latest version of Postgrez, come together to unlock a powerful new strategy for building, managing, and consuming Postgres extensions in a Kubernetes environment. By the end of this talk, my goal is that you will not only walk away with a streamlined and effective approach for getting your users the Postgres extensions they want and need, but I also want to end with a note about what this means for the Kubernetes platform and ecosystem as a whole. More specifically, I want to highlight how Kubernetes continues to influence the software we build in incredible new ways, sometimes 10 or even 20 plus years after its creation, as is the case for Postgres, as you will see today. So with that, let's now dig into exactly how Kubernetes image volumes enable a powerful new strategy for building, managing, and consuming Postgres extensions in your Kubernetes-based Postgres deployments.

So what exactly are Postgres extensions? At a h
