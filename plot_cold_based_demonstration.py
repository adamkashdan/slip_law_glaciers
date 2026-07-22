import numpy as np
import matplotlib.pyplot as plt

def generate_plot():
    # Setup vertical coordinate: z from -50m (bed) to +100m (ice)
    z_bed = np.linspace(-50, 0, 500)
    z_ice = np.linspace(0, 100, 1000)
    z = np.concatenate([z_bed, z_ice])

    # ─────────────────────────────────────────────────────────────────────────
    # 1. Warm-based Profile
    # ─────────────────────────────────────────────────────────────────────────
    # In the bed (z <= 0), velocity decays exponentially, showing shear penetration
    u_slip = 60.0  # m/yr sliding at interface
    d_bed = 15.0   # shear decay depth in permafrost (m)
    u_warm_bed = u_slip * np.exp(z_bed / d_bed)
    
    # In the ice (z > 0), standard internal deformation (Glen's law type flow)
    H_ice = 100.0
    u_df = 40.0    # internal deformation velocity (m/yr)
    u_warm_ice = u_slip + u_df * (1.0 - (1.0 - z_ice / H_ice)**4)
    u_warm = np.concatenate([u_warm_bed, u_warm_ice])

    # Shear strain rate (du/dz) for warm-based
    shear_warm_bed = (u_slip / d_bed) * np.exp(z_bed / d_bed)
    shear_warm_ice = (4.0 * u_df / H_ice) * (1.0 - z_ice / H_ice)**3
    shear_warm = np.concatenate([shear_warm_bed, shear_warm_ice])

    # ─────────────────────────────────────────────────────────────────────────
    # 2. Cold-based Profile
    # ─────────────────────────────────────────────────────────────────────────
    # In the bed (z <= 0), velocity is strictly 0 (frozen bed)
    u_cold_bed = np.zeros_like(z_bed)
    
    # In the ice (z > 0), shear is localized in a thin basal ice layer (e.g., 15m thick)
    # mimicking a cold thin glacier regime
    h_basal = 12.0
    u_max = 80.0   # max internal deformation velocity (m/yr)
    u_cold_ice = u_max * (1.0 - np.exp(-z_ice / h_basal))
    u_cold = np.concatenate([u_cold_bed, u_cold_ice])

    # Shear strain rate (du/dz) for cold-based
    shear_cold_bed = np.zeros_like(z_bed)
    shear_cold_ice = (u_max / h_basal) * np.exp(-z_ice / h_basal)
    shear_cold = np.concatenate([shear_cold_bed, shear_cold_ice])

    # ─────────────────────────────────────────────────────────────────────────
    # PLOTTING
    # ─────────────────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
    fig.patch.set_facecolor('#f4f1eb')

    c_warm = '#d45f1e' # warm-orange
    c_cold = '#2b7fb8' # cold-blue
    c_bed  = '#6e6255' # bedrock brown
    c_ice  = '#a5cbe3' # ice light blue

    # Left Panel: Warm-based glacier (deforming the permafrost bed)
    ax = axes[0]
    ax.set_facecolor('#faf8f4')
    ax.axhspan(-50, 0, color='#e2ded4', alpha=0.6, label='Subglacial Bed (Permafrost)')
    ax.axhspan(0, 100, color='#e8f3f8', alpha=0.6, label='Glacial Ice')
    
    # Plot velocity profile
    ax.plot(u_warm, z, color=c_warm, lw=3.0, label='Velocity $u(z)$')
    # Plot shear strain rate profile (dashed)
    ax.plot(shear_warm * 10, z, color='#888888', linestyle='--', lw=1.8, label='Shear Strain Rate $\dot{\epsilon}_{xz}$ (scaled)')
    
    ax.axhline(0, color='black', lw=1.5, linestyle=':')
    ax.set_title('A. Warm-Based Glacier (Sliding + Subglacial Shear)', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Velocity (m/yr) & Shear Rate (scaled)', fontsize=10)
    ax.set_ylabel('Vertical Coordinate $z$ (m, relative to bed)', fontsize=10)
    ax.set_xlim(-5, 120)
    ax.set_ylim(-45, 90)
    ax.grid(alpha=0.25)
    
    # Annotations
    ax.annotate('Significant basal slip\nat ice-bed interface', xy=(u_slip, 0), xytext=(u_slip + 10, 15),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.0), fontsize=9)
    ax.annotate('Shear penetrates bed\n→ Deforms massive ground ice', xy=(20, -15), xytext=(35, -25),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.0), fontsize=9, color='red')

    # Right Panel: Cold-based glacier (adhesive contact, preserving permafrost)
    ax = axes[1]
    ax.set_facecolor('#faf8f4')
    ax.axhspan(-50, 0, color='#e2ded4', alpha=0.6)
    ax.axhspan(0, 100, color='#e8f3f8', alpha=0.6)
    
    # Plot velocity profile
    ax.plot(u_cold, z, color=c_cold, lw=3.0, label='Velocity $u(z)$')
    # Plot shear strain rate profile (dashed)
    ax.plot(shear_cold * 10, z, color='#888888', linestyle='--', lw=1.8, label='Shear Strain Rate $\dot{\epsilon}_{xz}$ (scaled)')
    
    ax.axhline(0, color='black', lw=1.5, linestyle=':')
    ax.set_title('B. Cold-Based Glacier (Adhesive Contact, Preserved Bed)', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Velocity (m/yr) & Shear Rate (scaled)', fontsize=10)
    ax.set_xlim(-5, 120)
    ax.set_ylim(-45, 90)
    ax.grid(alpha=0.25)
    
    # Annotations
    ax.annotate('Zero slip at interface\n(Frozen to bed)', xy=(0, 0), xytext=(15, 8),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.0), fontsize=9)
    ax.annotate('Bed remains stationary ($u=0$)\n→ Relict massive ice preserved', xy=(0, -20), xytext=(20, -20),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.0), fontsize=9, color='green')
    ax.annotate('Shear localized in\nthin basal ice layer', xy=(40, 6), xytext=(55, 35),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.0), fontsize=9)

    # Shared legend
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=4, fontsize=9)

    fig.suptitle('Vertical Profiles of Velocity and Shear Strain Rate:\nWarm-Based vs. Cold-Based Glacial Regimes', 
                 fontsize=14, fontweight='bold', y=1.05)
    
    plt.tight_layout()
    plt.savefig('cold_based_shear_preservation.png', dpi=150, bbox_inches='tight')
    print("✓ Figure saved -> cold_based_shear_preservation.png")

if __name__ == '__main__':
    generate_plot()
