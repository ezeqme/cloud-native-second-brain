---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["Runtime Containers"]
speakers: ["Yusheng Zheng", "eunomia-bpf"]
sched_url: https://kccnceu2025.sched.com/event/1txFJ/ebpf-and-wasm-unifying-userspace-extensions-with-bpftime-yusheng-zheng-eunomia-bpf
youtube_search_url: https://www.youtube.com/results?search_query=eBPF+and+Wasm%3A+Unifying+Userspace+Extensions+With+Bpftime+CNCF+KubeCon+2025
slides: []
status: parsed
---

# eBPF and Wasm: Unifying Userspace Extensions With Bpftime - Yusheng Zheng, eunomia-bpf

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Yusheng Zheng, eunomia-bpf
- Schedule: https://kccnceu2025.sched.com/event/1txFJ/ebpf-and-wasm-unifying-userspace-extensions-with-bpftime-yusheng-zheng-eunomia-bpf
- Busca YouTube: https://www.youtube.com/results?search_query=eBPF+and+Wasm%3A+Unifying+Userspace+Extensions+With+Bpftime+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre eBPF and Wasm: Unifying Userspace Extensions With Bpftime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFJ/ebpf-and-wasm-unifying-userspace-extensions-with-bpftime-yusheng-zheng-eunomia-bpf
- YouTube search: https://www.youtube.com/results?search_query=eBPF+and+Wasm%3A+Unifying+Userspace+Extensions+With+Bpftime+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W5C0O7vk78o
- YouTube title: eBPF and Wasm: Unifying Userspace Extensions With Bpftime - Yusheng Zheng, eunomia-bpf
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ebpf-and-wasm-unifying-userspace-extensions-with-bpftime/W5C0O7vk78o.txt
- Transcript chars: 20772
- Keywords: kernel, extension, extensions, ebpf, interface, application, assembly, runtime, performance, safety, functions, isolation, version, verifier, program, called, software, security

### Resumo baseado na transcript

My name is Jun and I'm maintaining a bunch of EVPF related opensource projects in organization called Yomia BPF and I'm also a PhD student in Yoshi Santa Claus. Today I'm going to talk about something that has been around the software industry for a really long time. Even if it's not malicious external code can have bugs causing crashes, performance degression or security vulnerabilities. Uh for example, a few years back a popular video stream believe suffers a serious performance production outage because one of the engine's attention got stuck in an infinity loop. uh Apache HTTP server has similar issues where buff overflow bugs in ru based module can crash and security host like radius and a lot of applications. They also have things uh that really has or big companies and cost a lot of monies.

### Excerpt da transcript

Uh good afternoon everyone. My name is Jun and I'm maintaining a bunch of EVPF related opensource projects in organization called Yomia BPF and I'm also a PhD student in Yoshi Santa Claus. Today I'm going to talk about something that has been around the software industry for a really long time. as industless software extensions and introduce our use eBPF runtime called BPF time. Specifically, I want to talk about why we extensions, what make them challenging to handle correctly and how our current approach to manage extension might not be good enough. There will introduce a new approach to manage extensions called the extension interface model and our useless EPF runtime BPI time and how we implement this principles. Uh this so we have been maintaining the BPI time project for over two years. uh the research paper of it is 10 application safely and efficiently has recently been got accepted into OSBI this year. So uh there's a link you can Google search it or just visit it. [Music] Okay. So why we need to build a new EB use EBPF runtime?

Why we build this use EBPF runtime as yet another expansion framework? First software extensions are has a very long history. They included web servers, database editors and like VS code or and also some cloud native applications like Kubernetes extensions and web assembly models. In kernel they also have EBI programs and kernel modules. But there's a question a lot of people may ask. Why don't we just integrate everything into the main code bases? Why do we need to use extensions? The short answer is uh we need flex flexibility and isolation. We want flexibility and customization because it makes our software adaptable. User administrator want to tweak things to make meet their specific requirements without waiting for core developers to implement changes. But flexibility without isolation is risky. Extensions by definition they can be third party or at least externally developed code. You may trust your core engineering team but trusting external code is a different story. Even if it's not malicious external code can have bugs causing crashes, performance degression or security vulnerabilities.

So you need to protect your core applications. That's why main you need to is have extensions. But uh in real world extensions can be buggy. Uh for example, a few years back a popular video stream believe suffers a serious performance production outage because one of the engine's attention got stuck in an infinity loop. uh Apach
