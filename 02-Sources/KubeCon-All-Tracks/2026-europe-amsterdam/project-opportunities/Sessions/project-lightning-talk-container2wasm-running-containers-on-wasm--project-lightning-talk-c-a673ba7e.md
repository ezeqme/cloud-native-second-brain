---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Kohei Tokunaga", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwa/project-lightning-talk-container2wasm-running-containers-on-wasm-environments-kohei-tokunaga-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container2Wasm%3A+Running+Containers+On+Wasm+Environments+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Container2Wasm: Running Containers On Wasm Environments - Kohei Tokunaga, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kohei Tokunaga, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwa/project-lightning-talk-container2wasm-running-containers-on-wasm-environments-kohei-tokunaga-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container2Wasm%3A+Running+Containers+On+Wasm+Environments+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Container2Wasm: Running Containers On Wasm Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwa/project-lightning-talk-container2wasm-running-containers-on-wasm-environments-kohei-tokunaga-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container2Wasm%3A+Running+Containers+On+Wasm+Environments+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=z5NlfWd9p60
- YouTube title: Project Lightning Talk: Container2Wasm: Running Containers On Wasm Environments - Kohei Tokunaga
- Match score: 0.991
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-container2wasm-running-containers-on-wasm-envir/z5NlfWd9p60.txt
- Transcript chars: 3089
- Keywords: wasm, container, inside, llm, browser, running, backend, containers, command, recent, browsers, figure, compilation, support, testing, updates, runtimes, converter

### Resumo baseado na transcript

This is a tool to run Linux based containers in Wasm environment such as Wasm runtimes and browsers using Wasm compiled CPU emulators. The left figure shows the C2W command, which is a converter from a container to a Wasm blob. And in this demo, I've run VS Code for the web with VS Code LLM LLM let installed.

### Excerpt da transcript

Good morning everyone. I'm Kohei Tokunaga from NTT Inc. I'm a founding maintainer of container to Wasm. Today, I'm going to share some recent updates of this project. So, what is container to Wasm? This is a CNCF sandbox project since January 2025. This is a tool to run Linux based containers in Wasm environment such as Wasm runtimes and browsers using Wasm compiled CPU emulators. The left figure shows the C2W command, which is a converter from a container to a Wasm blob. You can run the con- converter's output on Wasm runtimes such as Wasm time for running the container. You can also run containers inside browsers as shown in the right figure. One of the recent updates is speeding up of the emulation performance. We've added a QEMU based JIT compilation backend for Wasm. The figure shows how does the JIT compilation backend speed up gzip compression in the container inside Wasm. QEMU based JIT backend complete the tasks task about three times faster comparing to the interpreter based backend. Also, in the QEMU community, there are discussions for Wasm support.

Uh QEMU version 10.1 added support for compilation into Wasm with its interpreter backend and the discussion for the JIT support is also ongoing. Uh we are recently exploring the use case of this project to LLM agent uh especially running fully inside browser, which is VS Code LLM let. This is an experimental extension for VS Code for the web, which is on browser VS Code. This runs LLMs on Wasm or WebGPU completely inside browser using llama.cpp. And the LLM is uh provided accesses to the workspace. So, the model can write files and code. Uh this extension also runs Linux based containers inside browser. The model can run shell commands in the container for testing the code completely inside browser. This also supports WebRTC based distributed inference across browsers. And in this demo, I've run VS Code for the web with VS Code LLM LLM let installed. I've used Qwen 3.5 4B in this demo. In the LLM let chat panel on the right, I've asked the model to create and test a mini uname command which just gets the kernel name from the uname syscall and just prints it.

The model is now creating a file which containing the implementation. The model has access to VS Code's file system APIs, so it can automatically create files by its own without my manual operation. And you can see the Linux terminal panel in the bottom. The model has access to this terminal, so it can test the code by its own without my manu
