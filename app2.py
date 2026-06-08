import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from mplsoccer import Pitch
import plotly.graph_objects as go

# 1. Configuração de Página do Dashboard
st.set_page_config(page_title="ARS Academy - Performance Hub", layout="wide")

st.title("🛡️ ARS Academy - Intelligence & Performance Hub")
st.markdown("Plataforma Executiva: Análise Estratégica para Cleverson (CEO), Reginaldo (Treinador) e Juresco (Treinador)")

# 2. LEITURA DOS BANCOS DE DADOS
df_scout = pd.read_excel("dados_jogadores_sub17.xlsx")
df_gps = pd.read_csv("telemetria_gps_bruta.csv")

# 3. FILTROS NA BARRA LATERAL
st.sidebar.header("Painel de Controle")
jogador_selecionado = st.sidebar.selectbox("Selecione o Atleta para Análise:", df_scout["Nome"].unique())
dados_linha = df_scout[df_scout["Nome"] == jogador_selecionado].iloc[0]

todas_metricas = [
    "Passes Progressivos", "Passes p/ Terço Final", "Ações Área Rival",
    "Duelos Ganhos (%)", "Recuperações Terço Rival", "Conduções Progressivas",
    "Interceptações", "xG (Gols Esperados)", "Desarmes"
]

metricas_selecionadas = st.sidebar.multiselect(
    "Métricas Visíveis na Teia:",
    options=todas_metricas,
    default=todas_metricas
)

# 4. CRIAÇÃO DAS ABAS DE CONTEÚDO
aba_teia, aba_gps = st.tabs(["📊 1. Perfil Técnico Consolidado (Scout)", "⚡ 2. Telemetria Física & GPS (Último Jogo)"])

# --- ABA 1: PERFIL TÉCNICO CONSOLIDADO ---
with aba_teia:
    if len(metricas_selecionadas) < 3:
        st.warning("⚠️ Selecione pelo menos 3 métricas na barra lateral para recalcular os ângulos do gráfico.")
    else:
        col1, col2 = st.columns([1.2, 1])
        
        with col1:
            # 1. DEFINIÇÃO DA ORDEM FIXA DAS MÉTRICAS
            # Ofensivas/Criação primeiro, Defensivas/Combate depois
            ordem_agrupada = [
                "xG (Gols Esperados)", 
                "Ações Área Rival", 
                "Passes p/ Terço Final", 
                "Passes Progressivos", 
                "Conduções Progressivas",
                "Recuperações Terço Rival", 
                "Duelos Ganhos (%)", 
                "Interceptações", 
                "Desarmes"
            ]
            
            # 2. REORDENAÇÃO DAS MÉTRICAS SELECIONADAS PARA RESPEITAR A ORDEM FIXA
            metricas_ordenadas = [m for m in ordem_agrupada if m in metricas_selecionadas]
            
            # (Opcional) Caso no futuro adicione métricas que não estão na lista acima, elas entram no final:
            metricas_ordenadas += [m for m in metricas_selecionadas if m not in ordem_agrupada]
            
            # 3. PUXANDO OS VALORES SEGUINDO ESSA NOVA ORDEM
            valores_taticos = [int(dados_linha[m]) for m in metricas_ordenadas]
            
            # 4. FECHANDO O CICLO DO RADAR COPIANDO O 1º VALOR E MÉTRICA PARA O FINAL
            valores_radar = valores_taticos + [valores_taticos[0]]
            metricas_radar = metricas_ordenadas + [metricas_ordenadas[0]]
            
            cores_pontos = ["#22c55e" if v >= 80 else "#eab308" if v >= 50 else "#ef4444" for v in valores_radar]
            
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=valores_radar,
                theta=metricas_radar,
                fill='toself',
                fillcolor='rgba(34, 197, 94, 0.2)', # Preenchimento verde com transparência
                line=dict(color='#22c55e', width=2),
                marker=dict(
                    size=10,
                    color=cores_pontos,
                    line=dict(color='white', width=1)
                ),
                hoverinfo="text",
                text=[f"{m}: {v}" for m, v in zip(metricas_radar, valores_radar)]
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100], # Trava a escala do gráfico de 0 a 100 (percentis)
                        gridcolor="#cbd5e1",
                        linecolor="#cbd5e1",
                        tickfont=dict(color="#475569")
                    ),
                    angularaxis=dict(
                        gridcolor="#cbd5e1",
                        linecolor="#cbd5e1",
                        tickfont=dict(size=12, color="#1e293b")
                    ),
                    bgcolor="#f8fafc"
                ),
                showlegend=False,
                title=dict(
                    text=f"<b>{jogador_selecionado}</b>",
                    x=0.5,
                    y=0.95,
                    font=dict(size=22, color="#1e293b")
                ),
                margin=dict(l=60, r=60, t=80, b=40)
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)
            
        with col2:
            st.subheader("📋 Relatório Estatístico Acumulado")
            st.markdown(f"**Atleta:** {jogador_selecionado} | **Pé Dominante:** {dados_linha['Pé Dominante']}")
            st.info("ℹ️ Os dados técnicos abaixo refletem a amostragem consolidada do bloco das últimas partidas da temporada.")
            
            # Bloco de Lateralidade do Naldo
            st.markdown("**🦶 Mapeamento de Ambidestria (Relatório Técnico Prof. Naldo):**")
            total_passes = dados_linha['Passes Pé Bom'] + dados_linha['Passes Pé Ruim']
            pct_pe_ruim_passes = int((dados_linha['Passes Pé Ruim'] / total_passes) * 100) if total_passes > 0 else 0
            
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                st.metric(label="Volume de Passes (Bom / Ruim)", value=f"{dados_linha['Passes Pé Bom']} / {dados_linha['Passes Pé Ruim']}")
            with col_f2:
                st.metric(label="Taxa de Uso do Pé Não Dominante", value=f"{pct_pe_ruim_passes}%")
            
            if pct_pe_ruim_passes < 10: 
                st.error("⚠️ Alta Previsibilidade. Atleta necessita de estímulo em treinos de fundamento.")
            elif pct_pe_ruim_passes < 20: 
                st.warning("📐 Evolução Regular. Padrão de distribuição em maturação.")
            else: 
                st.success("🎯 Perfil Ambidestro. Excelente variação de linhas de passe sob pressão.")
            
            st.markdown("**📈 Mapeamento de Competências vs. Média da Categoria (Percentil):**")
            for param in metricas_selecionadas:
                val = int(dados_linha[param])
                if val >= 80: st.success(f"**{param}:** {val}% (Elite)")
                elif val >= 50: st.warning(f"**{param}:** {val}% (Regular)")
                else: st.error(f"**{param}:** {val}% (Atenção)")

# --- ABA 2: POSICIONAMENTO & TELEMETRIA GPS ---
with aba_gps:
    st.subheader("🏃‍♂️ Volume Fisiológico & Ocupação Espacial")
    st.markdown("Métricas capturadas em tempo real na última partida através de sensores de alta frequência (10Hz).")
    
    col_gps1, col_gps2 = st.columns([1, 2])
    
    with col_gps1:
        st.markdown("**🔋 Índices Acumulados de Carga:**")
        st.metric(label="🏃‍♂️ Distância Total Percorrida", value=f"{dados_linha['Distância Total (km)']} km")
        st.metric(label="⚡ Sprints de Alta Intensidade (>24 km/h)", value=f"{dados_linha['Sprints (>24 km/h)']} sprints")
        st.info("💡 Análise de Desgaste: Dados úteis para o comissão técnica monitorar o balanço de carga e prevenção de lesões.")
        
    with col_gps2:
        dados_gps_jogador = df_gps[df_gps["Player_Name"] == jogador_selecionado]
        cx = dados_gps_jogador["X_Pitch (m)"].values
        cy = dados_gps_jogador["Y_Pitch (m)"].values

        pitch = Pitch(pitch_type='statsbomb', pitch_color='#1e3d1e', line_color='#ffffff', linewidth=1.5)
        fig_pitch, ax_pitch = pitch.draw(figsize=(8, 5))
        kde = pitch.kdeplot(cx, cy, ax=ax_pitch, cmap='YlOrRd', fill=True, thresh=0.01, alpha=0.6, n_levels=15)
        st.pyplot(fig_pitch)