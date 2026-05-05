---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability"]
speakers: ["Frederic Branczyk", "Polar Signals", "Natalie Serrino", "New Relic"]
sched_url: https://kccnceu2023.sched.com/event/1Hyak/past-present-and-future-of-ebpf-in-cloud-native-observability-frederic-branczyk-polar-signals-natalie-serrino-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Past%2C+Present%2C+and+Future+of+eBPF+in+Cloud+Native+Observability+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Past, Present, and Future of eBPF in Cloud Native Observability - Frederic Branczyk, Polar Signals & Natalie Serrino, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Frederic Branczyk, Polar Signals, Natalie Serrino, New Relic
- Schedule: https://kccnceu2023.sched.com/event/1Hyak/past-present-and-future-of-ebpf-in-cloud-native-observability-frederic-branczyk-polar-signals-natalie-serrino-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Past%2C+Present%2C+and+Future+of+eBPF+in+Cloud+Native+Observability+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Past, Present, and Future of eBPF in Cloud Native Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyak/past-present-and-future-of-ebpf-in-cloud-native-observability-frederic-branczyk-polar-signals-natalie-serrino-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Past%2C+Present%2C+and+Future+of+eBPF+in+Cloud+Native+Observability+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pb_eAVAWq2o
- YouTube title: Past, Present, & Future of eBPF in Cloud Native Observability - Frederic Branczyk & Natalie Serrino
- Match score: 0.83
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/past-present-and-future-of-ebpf-in-cloud-native-observability/pb_eAVAWq2o.txt
- Transcript chars: 32266
- Keywords: ebpf, actually, program, kernel, write, programs, reality, function, called, source, memory, present, observability, natalie, within, packet, symbols, machine

### Resumo baseado na transcript

all right let's get started then um so welcome to our session on past present and future of ebpf and observability um I'm joined by Natalie today from New Relic who is a contributor to the pixie open source project um I'm Frederick I founded a company called polar signals and we both happen to work on ebpf and in the context of observability so introduction to ebpf let's do a show of hands how many people know what ebpf is all right we see a lot of hands okay

### Excerpt da transcript

all right let's get started then um so welcome to our session on past present and future of ebpf and observability um I'm joined by Natalie today from New Relic who is a contributor to the pixie open source project um I'm Frederick I founded a company called polar signals and we both happen to work on ebpf and in the context of observability so introduction to ebpf let's do a show of hands how many people know what ebpf is all right we see a lot of hands okay so who's running some tools that use ebpf okay that's probably in maybe 50 percent who has written an ebpf program okay okay that's still maybe 20 30 that's actually more than I thought so um hopefully um at least by the end of uh this talk you'll will have everyone be able to raise their hand at the very least know how to write an ebpf program and how to get started with that obviously you won't have written a program yet um so just to make sure that we're all kind of on the same page of how ebpf works so ebpf is kind of a virtual machine within the Linux kernel um that we can attach to certain triggers so in this call in this case uh what we have is we're attaching an ebpf program that we've written below to some trigger and in this case it's whenever we execute the ciscal exec ve so every time this syscall is called first our ebpf program is called and we can do whatever we want um within within that context right we're getting given a bunch of con text about what's being executed and you know we can save that and you know have a counter of how often this Cisco is being called or we can do a log line or you know whatever is useful for us especially in the context of observability obviously we would want to kind of export some sort of signal so these hooks can vary very very very very widely and Natalie is kind of kind of teach us where all of this kind of originally came from but today there's a very wide variety of hooks that we could attach our ebpf programs to so that can be kernel probes so like attaching our program to a kernel function that's being executed you probes these can be used to kind of Trace user space execution so the programs that you and I write that run you know maybe written in go and they do I don't know some network service maybe some web server you could attach a probe to some function of your go program and also do some tracing with that or perf events this is actually something that I happen to work with on a daily basis so perf events tend to work in the way in a kind of
