---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Liam Randall", "Cosmonic"]
sched_url: https://kccncna2021.sched.com/event/lV1i/cloud-native-apps-with-server-side-webassembly-liam-randall-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Apps+with+Server-Side+WebAssembly+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Native Apps with Server-Side WebAssembly - Liam Randall, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Liam Randall, Cosmonic
- Schedule: https://kccncna2021.sched.com/event/lV1i/cloud-native-apps-with-server-side-webassembly-liam-randall-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Apps+with+Server-Side+WebAssembly+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Native Apps with Server-Side WebAssembly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1i/cloud-native-apps-with-server-side-webassembly-liam-randall-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Apps+with+Server-Side+WebAssembly+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2OTyBxPyW7Q
- YouTube title: Cloud Native Apps with Server-Side WebAssembly - Liam Randall, Cosmonic
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-native-apps-with-server-side-webassembly/2OTyBxPyW7Q.txt
- Transcript chars: 31110
- Keywords: assembly, running, application, technology, native, wasm, little, webassembly, security, taylor, applications, containers, business, non-functional, called, devices, second, locally

### Resumo baseado na transcript

Okay, well, good morning everyone and thank you so much for coming to cloud native apps with server side web assembly. I did an early Kubernetes company called Critical Stack that I sold to Capital One. And the key move that happened there is is that the security boundary moved from the box itself, you know, the Dell server, the IBM server, up to the CPU. And why am I doing this with my software applications, shipping entire operating systems?" So a virtualization layer, you know, containers was put together and coupled with Kubernetes it's really come to dominate the landscape. But we're going to talk a little bit about how the technology we technology we have today does not meet the challenges that we have today. But there are an increasing number of cases that do not depend on Linux nor will run Kubernetes.

### Excerpt da transcript

All right, guys. We're live. Let's get started. Okay, well, good morning everyone and thank you so much for coming to cloud native apps with server side web assembly. My name is Liam Randall and I have been in technology for a long time. I'm a serial entrepreneur and investor. I focused primarily in the open source space. I did Bro Zeek and then OS Query. I did an early Kubernetes company called Critical Stack that I sold to Capital One. And for the last few years I've been obsessed with web assembly and its implications for the cloud. I'm a hector man on Twitter. I'm on all the slacks and I try to be very accessible. So if you want to follow up with me afterwards, don't hesitate for a moment to ping me directly. So we're going to start with just a quick little summary of what web assembly is. This talk is not designed to teach you all about the details of web assembly. Instead, we're going to talk about how you can use web assembly on server side applications. But we do want to summarize to make sure we bring along as many people as possible with this along for the journey.

So web assembly is a little bit like some things that people have tried before. Strike stop me if this sounds familiar. You can write your apps once and run them anywhere. Of course you've heard that. Java, Silverlight, Flash. This promise has been made many times, but this time it's different. With web assembly we have an open W3 standard that's already supported on the devices you already use and love. All of your major browser vendors. It's incredibly efficient and fast and it's polyglot. Like it's not like Java. It doesn't come with its own programming language. It allows you to take code that you have and then recompile it down to this intermediate format. It runs everywhere. What's powerful about web assembly is is that these little engines, these wasm runtimes can be tuned for different circumstances. So for example, you might want to have your code running on big silicon in the cloud and you can have a web assembly runtime like wasm time that's tuned for that. Or perhaps you want to do some just in time compiling or ahead of time compiling out on the edge and you want to use it a runtime that's tuned for low power or low memory.

You can still use the same code and port them to both. So this is a very portable technology. And one of the most powerful things that we will talk about is that it's a very safe technology, but I'm going to hold that value prop for a moment. Let's ta
